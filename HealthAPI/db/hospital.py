from sqlalchemy import Column, String, UnicodeText

from HealthAPI.db import BASE


class Hospital(BASE):
    __table__ = "hospital"
    hostp_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    license = Column(String, nullable=False)
    address = Column(UnicodeText, nullable=False)

    def __repr__(self):
        return f"Hospital('{self.hostp_id}', '{self.name}')"


Hospital.__table__.create(checkfirst=True)
