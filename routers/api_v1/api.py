from fastapi import APIRouter
from .authentication import login, register

router = APIRouter()
"""
These routes are for authentication
-> login
-> register
"""
router.include_router(login.router, prefix="/auth", tags=["Login"])
router.include_router(register.router, prefix="/auth", tags=["Register"])
