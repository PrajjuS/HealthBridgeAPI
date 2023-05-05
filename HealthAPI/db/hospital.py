import threading

from sqlalchemy import Column, String, UnicodeText

from HealthAPI.db import BASE, SESSION
from HealthAPI.helpers import object_as_dict


class Hospital(BASE):
    __tablename__ = "hospital"
    hosp_id = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    license = Column(String, nullable=False)
    address = Column(UnicodeText, nullable=False)

    def __init__(
        self,
        hosp_id: str,
        password: str,
        name: str,
        license: str,
        address: str,
    ):
        self.hosp_id = hosp_id
        self.password = password
        self.name = name
        self.license = license
        self.address = address

    def __repr__(self):
        return f"Hospital('{self.hostp_id}', '{self.name}')"


Hospital.__table__.create(checkfirst=True)

HOSP_LOCK = threading.RLock()


def create_hosp(hosp_id: str, password: str, name: str, license: str, address: str):
    with HOSP_LOCK:
        hosp = Hospital(
            hosp_id=hosp_id,
            password=password,
            name=name,
            license=license,
            address=address,
        )
        SESSION.add(hosp)
        SESSION.commit()


def update_hosp(hosp_id: str, name: str, license: str, address: str):
    with HOSP_LOCK:
        hrow = SESSION.query(Hospital).get(hosp_id)
        hrow.name = name
        hrow.license = license
        hrow.address = address
        SESSION.commit()


def get_hinfo(hosp_id: str, is_dict: bool = False):
    try:
        res = SESSION.query(Hospital).filter(Hospital.hosp_id == hosp_id).first()
        if not is_dict:
            return res
        return object_as_dict(res)
    finally:
        SESSION.close()


def auth_huser(hosp_id: str, password: str):
    huser = get_hinfo(hosp_id)
    return huser.password == password


def check_huser(hosp_id: str):
    huser = get_hinfo(hosp_id)
    if huser:
        return True
    return False
