from pydantic import BaseModel


class HospitalMainModel(BaseModel):
    hosp_id: str
    password: str
    name: str
    license: str
    address: str


class NewHospitalModel(BaseModel):
    password: str
    name: str
    license: str
    address: str
