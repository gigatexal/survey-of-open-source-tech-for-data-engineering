from faker import Faker
from models.models import Book

import random

fake = Faker()

def no_dups(f):
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

@no_dups
def isbn()->str:
    return fake.isbn13()

@no_dups
def author()->str:
    return fake.name()

@no_dups
def title()->str:
    return fake.bs()

def price(lower=17, upper=99)->float:
    return random.randint(lower, upper) + (random.randint(0,99)/100)

#@no_dups
def new_book(title, author, price, isbn, version=1)->Book:
    kwargs = {
            'version': version,
            'title': title,
            'author': author,
            'price': price,
            'isbn': isbn}
    return Book(**kwargs)


