def errorMsg(msg, code, traceback=""):
    return {
        "status": {
            "isError": True,
            "code": code,
            "message": msg,
            "traceback": traceback,
        }
    }
