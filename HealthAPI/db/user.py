import datetime
import threading
from datetime import date, datetime

from sqlalchemy import (
    CHAR,
    BigInteger,
    Column,
    Date,
    DateTime,
    ForeignKey,
    String,
    UnicodeText,
    Integer
)
from sqlalchemy.orm import relationship

from HealthAPI.db import BASE, SESSION
from HealthAPI.helpers import object_as_dict


class User(BASE):
    __tablename__ = "user"
    user_id = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(CHAR, nullable=False)
    dob = Column(Date, nullable=False)
    bloodgroup = Column(String, nullable=False)
    mobile = Column(BigInteger, nullable=False)
    address = Column(String, nullable=False)
    reports = relationship("UserHealth", backref="hreport", lazy=True)

    def __init__(
        self,
        user_id: str,
        password: str,
        name: str,
        gender: str,
        dob: date,
        bloodgroup: str,
        mobile: str,
        address: str,
    ):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.gender = gender
        self.dob = dob
        self.bloodgroup = bloodgroup
        self.mobile = mobile
        self.address = address

    def __repr__(self):
        return f"User('{self.user_id}', '{self.name}')"


class UserHealth(BASE):
    __tablename__ = "user_reports"
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    report = Column(UnicodeText, nullable=False)
    user_id = Column(String, ForeignKey("user.user_id"), nullable=False)

    def __init__(self, date_time: datetime, report: str, user_id: str):
        self.date_time = date_time
        self.report = report
        self.user_id = user_id

    def __repr__(self):
        return f"UserHealth('{self.date_time}', '{self.id}')"


User.__table__.create(checkfirst=True)
UserHealth.__table__.create(checkfirst=True)


USER_LOCK = threading.RLock()


def create_user(
    user_id: str,
    password: str,
    name: str,
    gender: str,
    dob: date,
    bloodgroup: str,
    mobile: int,
    address: str,
):
    with USER_LOCK:
        user = User(
            user_id=user_id,
            password=password,
            name=name,
            gender=gender,
            dob=dob,
            bloodgroup=bloodgroup,
            mobile=mobile,
            address=address,
        )
        SESSION.add(user)
        SESSION.commit()


def update_user(
    user_id: str,
    name: str,
    gender: str,
    dob: date,
    bloodgroup: str,
    mobile: int,
    address: str,
):
    with USER_LOCK:
        urow = SESSION.query(User).get(user_id)
        urow.name = name
        urow.gender = gender
        urow.dob = dob
        urow.bloodgroup = bloodgroup
        urow.mobile = mobile
        urow.address = address
        SESSION.commit()


def get_uinfo(user_id: str, is_dict: bool = False):
    try:
        res = SESSION.query(User).filter(User.user_id == user_id).first()
        if not is_dict:
            return res
        return object_as_dict(res)
    finally:
        SESSION.close()


def auth_uuser(user_id: str, password: str):
    user = get_uinfo(user_id)
    return user.password == password


def check_uuser(user_id: str):
    user = get_uinfo(user_id)
    if user:
        return True
    return False


def create_ureport(user_id: str, date_time: datetime, report: str):
    with USER_LOCK:
        report = UserHealth(date_time=date_time, report=report, user_id=user_id)
        SESSION.add(report)
        SESSION.commit
