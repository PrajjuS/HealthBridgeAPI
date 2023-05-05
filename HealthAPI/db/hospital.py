from sqlalchemy import Column, String, UnicodeText

from HealthAPI.db import BASE


class Hospital(BASE):
    __table__ = "hospital"
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
        self.hostp_id = hosp_id
        self.password = password
        self.name = name
        self.license = license
        self.address = address

    def __repr__(self):
        return f"Hospital('{self.hostp_id}', '{self.name}')"


Hospital.__table__.create(checkfirst=True)
