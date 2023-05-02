from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
async def user_root():
    return {"message": "User route."}
