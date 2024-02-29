from pydantic import BaseModel, PositiveInt
from src.models.firms import Firm

class Commitment(BaseModel):
  id: PositiveInt
  asset_class: str
  firm_id: PositiveInt
  currency: str
  amount: str
