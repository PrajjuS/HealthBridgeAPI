from fastapi import APIRouter

router = APIRouter()


@router.get("/hospital")
async def hospital_root():
    return {"message": "Hospital route."}
