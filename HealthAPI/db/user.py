import datetime
from datetime import date, datetime

from sqlalchemy import (
    BigInteger,
    Column,
    Date,
    DateTime,
    ForeignKey,
    String,
    UnicodeText,
)
from sqlalchemy.orm import relationship

from HealthAPI.db import BASE


class User(BASE):
    __tablename__ = "user"
    user_id = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    mobile = Column(BigInteger, nullable=False)
    address = Column(String, nullable=False)
    reports = relationship("UserHealth", backref="hreport", lazy=True)

    def __init__(
        self,
        user_id: str,
        password: str,
        name: str,
        dob: date,
        mobile: str,
        address: str,
    ):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.dob = dob
        self.mobile = mobile
        self.address = address

    def __repr__(self):
        return f"User('{self.user_id}', '{self.name}')"


class UserHealth(BASE):
    __tablename__ = "user_reports"
    id = Column(primary_key=True)
    date_time = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
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
