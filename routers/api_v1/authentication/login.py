from fastapi import APIRouter, Depends
from schemas.request.request_auth_schemas import AuthLoginPayLoad
from models.user_models import User
from passlib.context import CryptContext
from config.database import get_db
from sqlalchemy.orm import Session
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/auth")


def get_password_hash(password):
    return pwd_context.hash(password)


@router.post("/login")
async def login(authloginpayload: AuthLoginPayLoad, db: Session = Depends(get_db)):

    create_user_model = User()
    create_user_model.username = authloginpayload.username
    # create_user_model.email = authloginpayload.email
    create_user_model.hashed_password = authloginpayload.password
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)
    return create_user_model
