# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint
class User(BaseModel):
 user_id: int
 name: constr(min_length=2, max_length=50)
 email: EmailStr
 age: conint(gt=18)
 # Restriction addedd to only let student_id have 8 digits and start with S
 student_id: constr(min_length=8, max_length=8, pattern="^S\d{7}$")
