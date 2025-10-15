from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

config = dotenv_values(".env")

client = MongoClient("ATLAS_URI", server_api=ServerApi('1'))
db = client.user_profiles
collection = db["users"]