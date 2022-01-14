from fastapi import FastAPI
from core.routes import api_router

app = FastAPI()

app.include_router(
    router=api_router
)


@app.post("/")
async def root():
    return {"message": "Hello World"}