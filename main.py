import json
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models.firms import Firm
from src.models.commitment import Commitment
from sqlalchemy import select, and_
import src.utils.asset_business_logic as asset_utils
from src.utils.db_utils import database, connect_to_db, disconnect_from_db
from src.models.db_models_metadata import firms, commitments

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_db()


@app.on_event("shutdown")
async def shutdown_event():
    await disconnect_from_db()


f = open("./db/data.json")
data = json.load(f)

INVESTOR_IDS: List[int] = []
FIRMS: List[Firm] = []
for firm in data["firms"]:
    INVESTOR_IDS.append(firm["firm_id"])
    parsed_firm = Firm(**firm)
    FIRMS.append(parsed_firm)


@app.get("/api/investors", response_model=list[Firm])
async def get_investors():
    query = firms.select()
    result = await database.fetch_all(query)
    
    # Convert the result set to Pydantic models
    investors = [Firm(**row) for row in result]
    return investors

@app.get("/api/investor/commitment/{asset_class}/{investor_id}")
async def get_commitments(investor_id: int, asset_class: str) -> List[Commitment]:
    print(investor_id,asset_class)
    query = select([commitments]).where(
        and_(
            commitments.c.asset_class == asset_class,
            commitments.c.firm_id == investor_id
        )
    )
    results = await database.fetch_all(query)
    commitments_list = [Commitment(**row) for row in results]
    return commitments_list 

