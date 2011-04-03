

class DBHelper(object):
    """Just a little helper for executing queries - somewhat friendlier then the DB API."""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
    
    def execute(self, sql, *params):
        self.cursor.execute(sql, *params)
        if self.cursor.description:
            return [RowHelper(row, self.cursor) for row in self.fetchall()]
    
    __call__ = execute

class RowHelper(object):
    def __init__(self, row, cursor):
        for i, col in enumerate(row):
            setattr(self, cursor.description[i][0], col)
    
    def __getitem__(self, attr):
        return getattr(self, attr)
        