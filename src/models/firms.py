from datetime import datetime
from pydantic import BaseModel, PositiveInt

class Firm(BaseModel):
  firm_id: PositiveInt
  firm_name: str
  AUM: PositiveInt
  date_added: datetime
  last_updated: datetime
  established_at: datetime
  firm_type: str
  city: str
  country: str
  address: str
  postal_code: str
  
