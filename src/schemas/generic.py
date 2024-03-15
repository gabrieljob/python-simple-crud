from db.database import Database

class Generic:
    def __init__(self, table):
        self.db = Database()
        self.cache = None
        self.table = table

    def create(self, args):
        keys = self.table['columns']
        keys.pop(0)
        sql = f"INSERT INTO {self.table['name']} ("

        i = 1

        for k in keys:
            sql = sql + f'{k}'

            if i < len(keys):
                sql = sql + ', '

            if i == len(keys):
                sql = sql + ')'

            i = i + 1

        i = 1

        sql = sql + ' VALUES ('

        for k in keys:
            sql = sql + f"'{args[k]}'"
            if i < len(keys):
                sql = sql + ', '

            if i == len(keys):
                sql = sql + ')'

            i = i + 1
            
        return self.db.rawSql(sql)
        
    
    def getAll(self):
        sql = f"SELECT * FROM {self.table['name']}"
        self.db.rawSql(sql)
        return self.db.result
    
    
    def getbyId(self, id):
        sql = f"SELECT * FROM {self.table['name']} WHERE id = {id}"
        self.db.rawSql(sql)

        if len(self.db.result) > 0:
            return self.db.result[0]
        
        return False
       

    def update(self, args):
        keys = self.table['columns']
        keys.pop(0)
        keys.pop(3)

        sql = f"UPDATE {self.table['name']} SET "
        i = 1

        for k in keys:
            sql = sql + f"{k} = '{args[k]}'"

            if i < len(keys):
                sql = sql + ', '

            i = i + 1

        sql = sql + f" WHERE id = {args['id']}"

        self.db.rawSql(sql)
        
    
    def delete(self, id):
        sql = f"DELETE FROM {self.table['name']} WHERE id = {id}"
        self.db.rawSql(sql)
        