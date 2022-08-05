"""Sample Api"""
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    """Class for typing person"""

    id: int
    name: str
    age: int


DB: List[Person] = [
    Person(id=1, name="Alice", age=14),
    Person(id=2, name="Bob", age=18),
    Person(id=3, name="Mike", age=20),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api")
async def api():
    return DB
