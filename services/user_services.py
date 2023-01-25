from services.main import AppService, AppCrud
from schemas.user_schemas import UserCreate
from models.models import User
from utils.auth_utils import get_hashed_password

class UserService(AppService):
    def __init__(self, db):
        self.db = db

    def create_user(self, item: UserCreate) -> AppService:
        users = UserCrud(self.db).create_user(item)
        return users


class UserCrud(AppCrud):
    def __init__(self, db):
        self.db = db

    def create_user(self, item: UserCreate) -> UserCreate:
        create_user_model = User()
        create_user_model.username = item.username
        create_user_model.hashed_password = get_hashed_password(item.password)
        self.db.add(create_user_model)
        self.db.commit()
        self.db.refresh(create_user_model)
        return create_user_model
