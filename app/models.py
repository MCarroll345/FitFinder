# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

class User(BaseModel):
    email:str
    first_name:str
    last_name:str


def individual_data(user):
    return{
        "id": str(user["_id"]),
        "email": user["email"],
        "first_name": user["first_name"],
        "last_name": user["last_name"]
    }


def all_users(users):
    return [individual_data(user) for user in users]