import json
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models.firms import Firm
from src.models.commitment import Commitment

import src.utils.asset_business_logic as asset_utils
from src.utils.db_utils  import connect_to_db, disconnect_from_db


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


@app.get("/api/investors", response_model=list[Firm])
async def get_investors():
  return asset_utils.get_investor_commitments_details

@app.get("/api/investor/commitment/{asset_class}/{investor_id}")
async def get_commitments(investor_id: int, asset_class: str) -> List[Commitment]:
    return asset_utils.get_investor_commitments_details

