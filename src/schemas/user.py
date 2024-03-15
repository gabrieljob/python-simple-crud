from schemas.generic import Generic
from utils.sqlToJson import sqlToJson

table = {'name': 'user', 'columns': ['id', 'name', 'bday', 'email', 'password']}

class User(Generic):
    def __init__(self):
        super().__init__(table)
    
    def getOneByFilter(self, filter):
        keys = filter
        sql = f"SELECT * FROM user WHERE "
        
        i = 1

        for k in keys:
            sql = sql + f"{k} = '{filter[k]}'"

            if i < len(keys):
                sql = sql + ' AND '

            i = i + 1
        
        self.db.rawSql(sql)
        
        if len(self.db.result) > 0:
            return sqlToJson(table['columns'], self.db.result)[0]
        
        return False