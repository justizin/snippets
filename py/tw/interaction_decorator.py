from functools import partial

def interaction(func):
    def wrap(self, *a, **kw):
        return self.dbpool.runInteraction(partial(func, self), *a, **kw)
    return wrap

class DatabaseRunner(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            'sqlite3', conf['database.sqlite.db_file'],
            check_same_thread=False)

    @interaction
    def get_repaste(self, txn, orig_url):
        pass
