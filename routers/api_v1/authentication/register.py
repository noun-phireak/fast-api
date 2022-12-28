from fastapi import APIRouter

router = APIRouter()


@router.get("/register")
async def register():
    return {
        "Message": "Register route found"
    }
