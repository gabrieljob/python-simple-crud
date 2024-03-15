import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.brinks'
DB_FILE = ROOT_DIR / DB_NAME

class Database:
    def __init__(self): 
        self.connection = None
        self.cursor = None
        self.result = None

    def connect(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

    def rawSql(self, sql):
        self.connect()
        result = self.cursor.execute(sql)
        self.result = result.fetchall()
        self.connection.commit()
        self.cursor.close()
        self.connection.close()