import mongoengine as me
from datetime import datetime
from src.models.commitment import Commitment
from src.models.firms import Firm

me.connect('AssetAnalytics', host='localhost', port=27017)
class CommitmentDocument(me.Document):
    id = me.IntField(primary_key=True)
    asset_class = me.StringField(required=True)
    firm_id = me.IntField(required=True)
    currency = me.StringField(required=True)
    amount = me.StringField(required=True)
    meta = {
        'collection': 'commitments',
        'indexes': [
            'id',
        ],
    }

class FirmDocument(me.Document):
    firm_id = me.IntField(primary_key=True)
    firm_name = me.StringField(required=True)
    AUM = me.IntField(required=True)
    date_added = me.DateTimeField(default=datetime.now)
    last_updated = me.DateTimeField()
    established_at = me.DateTimeField(required=True)
    firm_type = me.StringField(required=True)
    city = me.StringField(required=True)
    country = me.StringField(required=True)
    address = me.StringField(required=True)
    postal_code = me.StringField(required=True)
    meta = {
        'collection': 'firms',
        'indexes': [
            'firm_id',
        ],
    }



def get_all_firms():
    try:
        firms = FirmDocument.objects()
        if firms:
            return [firm.to_mongo().to_dict() for firm in firms]
        else:
            return None
    except me.ValidationError as e:
        print(f"Error: {e}")
        return None


def select_firm_by_id(firm_id):
    try:
        firm = FirmDocument.objects(firm_id=firm_id).first()
        if firm:
            return firm.to_mongo().to_dict() 
        else:
            return None
    except me.ValidationError as e:
        print(f"Error: {e}")
        return None

# Function to perform a select query on the Commitment collection
def select_commitments_by_firm_id(firm_id,asset_class):
    try:
        commitments = CommitmentDocument.objects(firm_id=firm_id, asset_class=asset_class)
        return [commitment.to_mongo().to_dict() for commitment in commitments]
    except me.ValidationError as e:
        print(f"Error: {e}")
        return []
