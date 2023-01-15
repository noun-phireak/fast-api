from fastapi import APIRouter

router = APIRouter(prefix="/auth")


@router.get("/register")
async def register():
    return {
        "Message": "Register route found"
    }
