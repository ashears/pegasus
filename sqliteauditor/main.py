from pydantic import BaseModel, FilePath
from typing import List
import sqlite3
import os
from pathlib import Path


class Table(BaseModel):
    create_if_not_found: bool = False
    table_name: str


class Database(BaseModel):
    path: FilePath
    tables: List[Table]


class SqliteAuditor:
    # def __init__(self,
    #              database_path: str,
    #              create_db_if_not_found: bool = True):
    #     self.create_db_if_not_found = create_db_if_not_found
        # self.database_path = database_path

        # if not os.path.isfile(self.database_path) and self.create_if_not_found is False:
        #    raise Exception('Database does not exist')
        # Path(self.database_path).touch()
        # sqlite3.connect(self.database_path)

    @classmethod
    def audit_database(cls, database: Database, validate_rows: False):
        if not os.path.isfile(database.path) and self.create_db_if_not_found is False:
            raise Exception('Database does not exist')
        with sqlite3.connect(database.path) as connection:
            connection.row_factory = sqlite3.Row
            cur = connection.cursor()
        pass

    def audit_table(self, database_path: str, table_name: str, validate_rows: False):
        if not os.path.isfile(database_path) and self.create_db_if_not_found is False:
            raise Exception('Database does not exist')
        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row
            cur = connection.cursor()
            if validate_rows:
                pass
                # return self.table_valid(self, table_name)
            else:
                return self.table_exists(cur, table_name)

    def table_exists(self, cur, database_path: str, table_name: str):
        stmt = "SHOW TABLES LIKE ?"
        cur.execute(stmt, (table_name,))
        result = cur.fetchone()
        if result:
            return True
        return False

    def table_rows_valid(self, table_name, table_rows: List[str]):
        if not os.path.isfile(self.database_path) and self.create_db_if_not_found is False:
            raise Exception('Database does not exist')
        with sqlite3.connect(self.database_path) as connection:
            connection.row_factory = sqlite3.Row
            cur = connection.cursor()
            stmt = "SHOW TABLES LIKE ?"
            cur.execute(stmt, (table_name,))
            result = cur.fetchone()
            if result:
                return True
            return False

    # there are no tables named "tableName"
    # def process_table(self,
    #                   table: Table,
    #                   create_if_not_found: bool = False):
    #     with sqlite3.connect(self.database_path) as connection:
    #         connection.row_factory = sqlite3.Row
    #         cur = connection.cursor()
    #         c.execute("SELECT * FROM ?", (table.table_name,))
    #         output = c.fetchall())
    #     pass


if __name__ == "__main__":
    class tab(Table):
        col1: str
        col2: str
    tab(table_name="", col1="1", col2="2")




