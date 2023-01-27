from pydantic import BaseModel

class Book(BaseModel):
    version: int
    _type: str = 'book'
    title: str
    author: str
    price: float
    isbn: str
