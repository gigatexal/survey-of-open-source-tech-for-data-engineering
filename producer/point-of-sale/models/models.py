from pydantic import BaseModel

class HashableBaseModel(BaseModel):
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

class Book(HashableBaseModel):
    version: int
    _type: str = 'book'
    title: str
    author: str
    price: float
    isbn: str
