from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)


def test_get_commitments_invalid_investor():
    invalid_investor_id = 999 
    asset_class = 'neg'
    response = client.get(f"/api/investor/commitment/{asset_class}/{invalid_investor_id}")
    assert response.status_code == 404

def test_get_commitments_invalid_asset_class():
    investor_id = 332  
    invalid_asset_class = 'unknown'
    response = client.get(f"/api/investor/commitment/{invalid_asset_class}/{investor_id}")
    assert response.status_code == 404

