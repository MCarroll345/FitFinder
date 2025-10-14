from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Book, BookUpdate

router = APIRouter()

@router.post("/", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=users)
def create_book(request: Request, user: users = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["user"].insert_one(user)
    created_user = request.app.database["user"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user

@router.get("/", response_description="List all books", response_model=List[users])
def list_users(request: Request):
    user = list(request.app.database["user"].find(limit=100))
    return user

@router.get("/{id}", response_description="Get a single book by id", response_model=users)
def find_user(id: str, request: Request):
    if (user := request.app.database["user"].find_one({"_id": id})) is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}
    if len(book) >= 1:
        update_result = request.app.database["books"].update_one(
            {"_id": id}, {"$set": book}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

    if (
        existing_book := request.app.database["books"].find_one({"_id": id})
    ) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")