from flask import request
from typing import List
from src.models.firms import Firm
from src.models.commitment import Commitment
import json
from src.utils.constants import ASSET_CLASSES
import src.utils.db_utils as db_utils


def get_all_investor_funds()->List[Firm]:
    firms = db_utils.get_all_firms()
    FIRMS: List[Firm] = []
    for firm in firms:
        parsed_firm = Firm(**firm)
        FIRMS.append(parsed_firm)
    return FIRMS



def get_investor_commitments_details()-> List[Commitment]:
    firms = db_utils.get_all_firms()
    INVESTOR_IDS: List[int]= []
    for firm in firms:
        INVESTOR_IDS.append(firm["firm_id"])
    if request.investor_id not in INVESTOR_IDS:
        raise Exception(status_code=404, detail=f"investor with id {request.investor_id} not found")
    if request.asset_class not in ASSET_CLASSES:
        raise Exception(status_code=404, detail=f"asset class {request.asset_class} does not exist")
    result: List[Commitment] = []
    commitments = db_utils.select_commitments_by_firm_id(request.insestor_id, request.asset_class)
    for commitment in commitments :
        # if commitment["firm_id"] == request.investor_id and commitment["asset_class"] == request.asset_class:
            parsed_commitment = Commitment(**commitment)
            result.append(parsed_commitment)
    return result
