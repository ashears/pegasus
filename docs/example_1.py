import sys
sys.path.append("../..")
from sqliteauditor import SqliteAuditor, Table
from pydantic import SecretStr


class UsersTable(Table):
    username: str
    password: SecretStr


result, result_msg = SqliteAuditor.audit_database(db="tmp/database.db",
                                                  table_schemas=[UsersTable])
