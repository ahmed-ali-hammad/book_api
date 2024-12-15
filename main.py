from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/health")
async def health():
    return {"message": "App is healthy"}, 200


@app.get("/greet/{name}")
async def greet(name: str, age: Optional[int] = None) -> str:
    if not age:
        return f"Hello {name}"
    return f"Hello {name}, you are {age} years old"
