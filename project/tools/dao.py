from sqlalchemy.orm.scoping import scoped_session


class BaseDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session
