import uuid
from typing import Optional
from pydantic import BaseModel, Field

class users(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "email": "email.abc@email.com",
                "first_name": "John",
                "last_name": "MongoDB"
            }
        }

class BookUpdate(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "email": "email.abc@email.com",
                "first_name": "John",
                "last_name": "MongoDB"
            }
        }