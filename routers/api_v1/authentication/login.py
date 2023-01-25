from fastapi import APIRouter, Depends
from schemas.user_schemas import UserCreate
from services.user_services import UserService
from models.models import User
from config.database import get_db
from sqlalchemy.orm import Session
from utils.auth_utils import get_hashed_password

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(item: UserCreate, db: get_db = Depends()):
    result = UserService(db).create_user(item)
    return result
