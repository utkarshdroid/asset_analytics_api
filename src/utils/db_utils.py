from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:@host.docker.internal:8005/asset_analytics"
database = Database(DATABASE_URL)

metadata = MetaData()

async def connect_to_db():
    await database.connect()
    print("Database connected.")

async def disconnect_from_db():
    await database.disconnect()
    print("Database disconnected.")