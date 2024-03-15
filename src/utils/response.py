def exception(e):
    return {
        "message": "Something went wrong",
        "data": None,
        "error": str(e)
    }, 500
    
def ok(data, message = 'Ok', statusCode = 200):
    return {
        "message": message,
        "data": data
    }, statusCode