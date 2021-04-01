
from peewee import SqliteDatabase

from os import getcwd

class DataBaseHandler:
    db_path = getcwd() + "/plugins/toolsbox/WebTools/tools/UrlFuzzer/assets/data.db"
    db_main = SqliteDatabase(db_path)

    def connect(self):
        self.db_main.connect()

    def close(self):
        self.db_main.close()
