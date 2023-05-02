from fastapi import FastAPI

app = FastAPI()

__version__ = "BETA"


@app.get("/")
async def root():
    return {"message": f"API is up with version {__version__}"}
