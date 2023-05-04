import datetime

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
    address = Column(String, nullable=False)
    mobile = Column(BigInteger, nullable=False)
    reports = relationship("UserHealth", backref="hreport", lazy=True)

    def __repr__(self):
        return f"User('{self.user_id}', '{self.name}')"


class UserHealth(BASE):
    __tablename__ = "user_reports"
    id = Column(primary_key=True)
    date_time = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    report = Column(UnicodeText, nullable=False)
    user = Column(String, ForeignKey("user.user_id"), nullable=False)

    def __repr__(self):
        return f"UserHealth('{self.date_time}', '{self.id}')"


User.__table__.create(checkfirst=True)
UserHealth.__table__.create(checkfirst=True)
