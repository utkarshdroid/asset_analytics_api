from typing import List
from src.models.firms import Firm
from src.models.commitment import Commitment
from fastapi import FastAPI, HTTPException
from src.utils.constants import ASSET_CLASSES
import src.utils.db_utils as db_utils
from sqlalchemy import select, and_
from src.models.db_models_metadata import firms, commitments
from src.utils.db_utils import database, connect_to_db, disconnect_from_db


async def get_all_investor_funds() -> List[Firm]:
    query = firms.select()
    result = await database.fetch_all(query)
    investors = [Firm(**row) for row in result]
    return investors


async def get_investor_commitments_details(
    investor_id: int, asset_class: str
) -> List[Commitment]:
    if asset_class not in ASSET_CLASSES:
        raise HTTPException(
            status_code=404, detail=f"Asset class '{asset_class}' does not exist"
        )

    query = select([commitments]).where(
        and_(
            commitments.c.asset_class == asset_class,
            commitments.c.firm_id == investor_id,
        )
    )
    results = await database.fetch_all(query)

    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No commitments found for investor ID {investor_id} in asset class '{asset_class}'",
        )
    commitments_list = [Commitment(**row) for row in results]
    return commitments_list
