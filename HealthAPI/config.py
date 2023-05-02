from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(f"{Path(__file__).parents[1]}/config.env")


class Config:
    TEMP: str = environ.get("TEMP", "Temporary")
