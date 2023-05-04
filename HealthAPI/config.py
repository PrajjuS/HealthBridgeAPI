from os import environ
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(f"{Path(__file__).parents[1]}/config.env")


class Config:
    try:
        DB_URI: str = environ.get("DB_URI")
    except Exception:
        print("DB_URI config not found.\nExiting..")
        exit()
