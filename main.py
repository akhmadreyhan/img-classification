from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import extract

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

@app.get("/")

def root():
    return {"hello":"world"}

app.include_router(extract.router)