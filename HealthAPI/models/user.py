from datetime import date

from pydantic import BaseModel


class UserMainModel(BaseModel):
    user_id: str
    password: str
    name: str
    gender: str
    dob: date
    bloodgroup: str
    mobile: int
    address: str
