from fastapi import FastAPI

app = FastAPI()

__version__ = "BETA"


@app.get("/")
async def root():
    return {"message": f"HealthAPI {__version__} is up."}
