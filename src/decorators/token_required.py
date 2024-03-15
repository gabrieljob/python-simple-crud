from functools import wraps
from flask import request
from utils.token import decode
from utils.sqlToJson import sqlToJson
from schemas.user import User, table

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        user = User()
        
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
            
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            token = decode(token)
            current_user = sqlToJson(table['columns'], [user.getbyId(token['id'])])[0]
            del current_user['password']
            
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
            
        return f(current_user, *args, **kwargs)

    return decorated