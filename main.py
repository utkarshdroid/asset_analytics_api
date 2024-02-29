import json
from flask import Flask ,request, htt
import utils.asset_business_logic as asset_utils
from utils.common import errorMsg

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_exception(e):
    if not hasattr(request,'exception_caused'):
        request.exception_caused =[]
    request.exception_caused.append({
        'func': "handle_exception",
        "error":str(e)
    })
    return errorMsg("API call Fail", 500, traceback=e)

@app.get("/api/investors")
def get_investors():
  return asset_utils.get_all_investor_funds()

@app.get("/api/investor/commitment/{asset_class}/{investor_id}")
def get_commitments():
  request.asset_class = request.args.get('asset_class','')
  request.investor_id = request.args.get('investor_id','')
  return asset_utils.get_investor_commitments_details()
  
@app.after_request
def log_api_response():
  pass

if __name__ =="__main__":
  app.run(host='0.0.0.0',port=8000,debug=True)