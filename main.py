from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel


class BookCreateModel(BaseModel):
    title: str
    author: str


app = FastAPI()


@app.get("/health")
async def health():
    return {"message": "App is healthy"}, 200


@app.get("/greet/{name}")
async def greet(name: str, age: Optional[int] = None) -> str:
    if not age:
        return f"Hello {name}"
    return f"Hello {name}, you are {age} years old"


@app.post("/create_book")
async def create_book(data: BookCreateModel):
    return {"Book Title": data.title, "Book Author": data.author}


@app.get("/get_headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
):
    return {"ACCEPT": accept, "CONTENT-TYPE": content_type, "USER-AGENT": user_agent}
