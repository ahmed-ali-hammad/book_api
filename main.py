from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


@app.get("/health", status_code=200)
async def health():
    return {"message": "App is healthy"}


@app.get("/books", response_model=List[Book])
async def get_all_books() -> list:
    """Returns a list of all available books"""
    with open("books.json", "r") as f:
        books = json.load(f)
    return books


@app.post("/books")
async def create_book():
    """Create a new book"""
    return


@app.put("/book/{book_id}")
async def update_book():
    """Update a book"""
    return


@app.delete("/book/{book_id}")
async def delete_book():
    """delete a book"""
    return
