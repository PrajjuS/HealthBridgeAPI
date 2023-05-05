from fastapi import APIRouter

from HealthAPI.db.hospital import auth_huser, check_huser
from HealthAPI.db.user import (
    auth_uuser,
    check_uuser,
    create_ureport,
    create_user,
    get_uinfo,
    get_ureports,
    update_user,
)
from HealthAPI.helpers import Error, generate_id
from HealthAPI.models import NewUserModel, UserMainModel

router = APIRouter()


def check_and_auth(hosp_id: str, h_pass):
    if not check_huser(hosp_id):
        return Error.HOSPITAL_NOT_FOUND
    if not auth_huser(hosp_id, h_pass):
        return Error.INVALID_HOSPITAL_AUTH


@router.get("/user")
async def user_root():
    return {"message": "User route."}


@router.get(
    "/user/info",
    response_model_exclude={"password"},
)
async def user_info(hosp_id: str, h_pass: str, user_id: str):
    check_and_auth(hosp_id, h_pass)
    if res := get_uinfo(user_id, is_dict=True):
        return {**res, "reports": get_ureports(user_id)}
    return Error.USER_NOT_FOUND


@router.post(
    "/user/create",
    response_model=UserMainModel,
    response_model_exclude={"password"},
)
async def user_create(hosp_id: str, h_pass: str, details: NewUserModel):
    check_and_auth(hosp_id, h_pass)
    create_user(
        id := generate_id(details.name, 6),
        details.password,
        details.name,
        details.gender,
        details.dob,
        details.bloodgroup,
        details.mobile,
        details.address,
    )
    return {"user_id": id, **details.dict()}


@router.patch(
    "/user/update",
    response_model=UserMainModel,
    response_model_exclude={"password"},
)
async def user_create(hosp_id: str, h_pass: str, details: UserMainModel):
    check_and_auth(hosp_id, h_pass)
    if not check_uuser(details.user_id):
        return Error.USER_NOT_FOUND
    if not auth_uuser(details.user_id, details.password):
        return Error.INVALID_USER_AUTH
    update_user(
        details.user_id,
        details.name,
        details.gender,
        details.dob,
        details.bloodgroup,
        details.mobile,
        details.address,
    )
    return details


@router.post("/user/report")
async def user_report(
    hosp_id: str,
    h_pass: str,
    user_id: str,
    u_pass: str,
    report: str,
):
    check_and_auth(hosp_id, h_pass)
    if not check_uuser(user_id):
        return Error.USER_NOT_FOUND
    if not auth_uuser(user_id, u_pass):
        return Error.INVALID_USER_AUTH
    create_ureport(user_id, report)
    return {"user_id": user_id, "report": report}
