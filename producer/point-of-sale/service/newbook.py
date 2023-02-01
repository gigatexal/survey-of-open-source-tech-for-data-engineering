from faker import Faker
from models.models import Book

import random

fake = Faker()

def inmem_dedup(f):
    s = set()
    def wrap(*args, **kwargs):
        while True:
            if (item:=f(*args, **kwargs)) not in s:
                print(f"trying to add item {item} to set, with set items {s}")
                s.add(item)
                return item
            else:
                continue
    return wrap


def db_dedup(f):
    import sqlite3 as db
    import tempfile
    # TODO: implement
    # just store the __hash__() of a given object
    pass
    


@inmem_dedup
def isbn()->str:
    return fake.isbn13()

@inmem_dedup
def author()->str:
    return fake.name()

@inmem_dedup
def title()->str:
    return fake.bs()

def price(lower=17, upper=99)->float:
    return random.randint(lower, upper) + (random.randint(0,99)/100)

@inmem_dedup
def new_book(title, author, price, isbn, version=1)->Book:
    return Book(
            title=title,
            author=author,
            price=price,
            isbn=isbn,
            version=version)


