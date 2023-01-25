from sqlalchemy.orm import Session


class DBSessionContext(object):
    def __int__(self, db: Session):
        self.db = db


class AppService(DBSessionContext):
    pass


class AppCrud(DBSessionContext):
    pass
