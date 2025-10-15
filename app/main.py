from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .routes import router as user_router

config = dotenv_values(".env")

app = FastAPI()

client = MongoClient("ATLAS_URI", server_api=ServerApi('1'))
db = client.user_profiles


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(user_router, prefix="/user")