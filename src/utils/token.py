import jwt

def encode(data):
    return jwt.encode(data, "secret", algorithm="HS256")

def decode(token):
    return jwt.decode(token, "secret", algorithms="HS256")