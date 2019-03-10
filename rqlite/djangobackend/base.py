"""
SQLite3 backend for the sqlite3 module in the standard library.
"""


from django.db.backends.sqlite3.base import *
import pyrqlite.dbapi2 as Database
from pyrqlite.cursors import Cursor as DBCursor

Database.Cursor = DBCursor

class RqliteWrapper(DatabaseWrapper):
    vendor = 'rqlite'
    display_name = 'RQLite'
    Database = Database

    def get_connection_params(self):
        opts = self.settings_dict['OPTIONS']
        ret = {'host': opts.get('HOST', 'localhost'),
               'port': opts.get('PORT', 4001)}
        return ret

    def get_new_connection(self, conn_params):
        conn = Database.connect(**conn_params)
        return conn

    def create_cursor(self, name=None):
        return self.connection.cursor(factory=RqliteCursorWrapper)

    def _start_transaction_under_autocommit(self):
        """
        Start a transaction explicitly in autocommit mode.

        Staying in autocommit mode works around a bug of sqlite3 that breaks
        savepoints when autocommit is disabled.
        """
        pass


class RqliteCursorWrapper(DBCursor):
    """
    Django uses "format" style placeholders, but pysqlite2 uses "qmark" style.
    This fixes it -- but note that if you want to use a literal "%s" in a query,
    you'll need to use "%%s".
    """
    def execute(self, query, params=None):
        if params is None:
            return Database.Cursor.execute(self, query)
        query = self.convert_query(query)
        return Database.Cursor.execute(self, query, params)

    def executemany(self, query, param_list):
        query = self.convert_query(query)
        return Database.Cursor.executemany(self, query, param_list)

    def convert_query(self, query):
        return FORMAT_QMARK_REGEX.sub('?', query).replace('%%', '%')


DatabaseWrapper = RqliteWrapper
