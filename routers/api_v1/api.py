from fastapi import APIRouter
from .authentication import login, register

router = APIRouter(prefix="/api/v1")


"""
These routes are for authentication
-> login
-> register
"""
router.include_router(login.router, tags=["Login"])
router.include_router(register.router, tags=["Register"])
