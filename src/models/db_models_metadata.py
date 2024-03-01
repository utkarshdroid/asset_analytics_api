from sqlalchemy import Table, Column, Integer, String, DateTime, create_engine, MetaData

metadata = MetaData()

firms = Table(
    "firms", metadata,
    Column("firm_id", Integer, primary_key=True),
    Column("firm_name", String),
    Column("aum", String),
    Column("date_added", DateTime),
    Column("last_updated", DateTime),
    Column("established_at", DateTime),
    Column("firm_type", String),
    Column("city", String),
    Column("country", String),
    Column("address", String),
    Column("postal_code", String),
    schema='info'
)

commitments = Table(
    "commitments", metadata,
    Column("id", Integer, primary_key=True),
    Column("asset_class", String),
    Column("firm_id", Integer),
    Column("currency", String),
    Column("amount", String),
    schema='info'
)
