import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isEmailValid(email):
    if re.fullmatch(regex, email):
      return bool(1)
    else:
      return bool()