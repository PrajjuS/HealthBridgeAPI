from fastapi import FastAPI

from HealthAPI.routes import hrouter, urouter

app = FastAPI()

__version__ = "BETA"

app.include_router(hrouter)
app.include_router(urouter)


@app.get("/")
async def root():
    return {"message": f"HealthAPI {__version__} is up."}
