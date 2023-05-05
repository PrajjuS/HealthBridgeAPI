from fastapi import APIRouter

from HealthAPI.db.hospital import (
    auth_huser,
    check_huser,
    create_hosp,
    get_hinfo,
    update_hosp,
)
from HealthAPI.helpers import Error, generate_id
from HealthAPI.models import HospitalMainModel, NewHospitalModel

router = APIRouter()


@router.get("/hospital")
async def hospital_root():
    return {"message": "Hospital route."}


@router.get(
    "/hospital/info",
    response_model=HospitalMainModel,
    response_model_exclude={"password"},
)
async def hosp_info(hosp_id: str):
    if res := get_hinfo(hosp_id, is_dict=True):
        return {**res}
    return Error.USER_NOT_FOUND


@router.post(
    "/hospital/create",
    response_model=HospitalMainModel,
    response_model_exclude={"password"},
)
async def hosp_create(master_pass: str, details: NewHospitalModel):
    if not master_pass == "WeBrogrammers":
        return Error.INVALID_MASTER_AUTH
    create_hosp(
        id := generate_id(details.name, 9),
        details.password,
        details.name,
        details.license,
        details.address,
    )
    return {"hosp_id": id, **details.dict()}


@router.patch(
    "/hospital/update",
    response_model=HospitalMainModel,
    response_model_exclude={"password"},
)
async def hosp_update(details: HospitalMainModel):
    if not check_huser(details.hosp_id):
        return Error.HOSPITAL_NOT_FOUND
    if not auth_huser(details.hosp_id, details.password):
        return Error.INVALID_HOSPITAL_AUTH
    update_hosp(
        details.hosp_id,
        details.name,
        details.license,
        details.address,
    )
    return details
