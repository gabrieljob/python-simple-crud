from schemas.user import User, table
from flask import Flask, make_response, request
from utils.md5 import formatToMd5
from utils.validation.email import isEmailValid
from utils.token import encode
from utils.sqlToJson import sqlToJson
from utils.response import exception, ok
from decorators.token_required import token_required

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request_func(data):
    response = make_response(data)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/v1/user', methods=['GET'])
@token_required
def getAllUser(current_user):
    try:
        user = User()
        results = user.getAll()
        results = sqlToJson(table['columns'], results)

        for r in results:
            del r['password']
        
        return ok(results)
    except Exception as e:
        return exception(e)

@app.route('/api/v1/user/<int:id>', methods=['GET'])
@token_required
def getUserById(current_user, id):
    try:
        user = User()
        result = user.getbyId(id)
        result = sqlToJson(table['columns'], [result])[0]
        del result['password']
        return ok(result)
    except Exception as e:
        return exception(e)

@app.route('/api/v1/user/<int:id>', methods=['DELETE'])
@token_required
def deleteUser(current_user, id):
    try:
        user = User()
        user.delete(id)
        return ok(None, 'Success', 201)
    except Exception as e:
        return exception(e)

@app.route('/api/v1/user', methods=['POST'])
@token_required
def createUser(current_user):
    try:
        user = User()
        data = request.form.to_dict()
        data['password'] = formatToMd5(data['password'])
        
        if not isEmailValid(data['email']):
            raise Exception('Malformed Email Rejected')
        
        isUserAlreadyRegistered = user.getOneByFilter({ 'email': data['email']})  
            
        if isUserAlreadyRegistered:
            raise Exception('User already registered')
        
        user.create(data)
        return ok(None, 'Created', 201)
    except Exception as e:
        return exception(e)

@app.route('/api/v1/user', methods=['PUT'])
@token_required
def updateUser(current_user):
    try:
        user = User()
        data = request.form.to_dict()
        del data['password']
        
        if not isEmailValid(data['email']):
            raise Exception('Malformed Email Rejected')
        
        user.update(data)
        return ok(None, 'Created', 201)
    except Exception as e:
        return exception(e)

@app.route('/api/v1/login', methods=['POST'])
def login():
    try:
        user = User()
        data = request.form.to_dict()
        
        if not isEmailValid(data['email']):
            return 'Malformed Email Rejected'
        
        data['password'] = formatToMd5(data['password'])
        
        result = user.getOneByFilter({ 'email': data['email'], 'password': data['password'] })
        del result['password']
        
        return ok(encode(result), 'Created', 201)
    except Exception as e:
        return exception(e)

if __name__ == '__main__':
    app.run()