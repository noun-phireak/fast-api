from pydantic import BaseModel
from typing import Optional


class AuthLoginPayLoad(BaseModel):
    username: str
    # email: Optional[str]
    password: str

    class Config:
        allow_extra = True