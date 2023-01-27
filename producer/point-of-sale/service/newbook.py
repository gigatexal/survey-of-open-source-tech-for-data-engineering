from faker import Faker
from models.models import Book

fake = Faker()

def no_dups(f):
    s = set()
    def wrap(*args, **kwargs):
        while True:
            if (item:=f(*args, **kwargs)) not in s:
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


def new_book(**kwargs)->Book:
    return Book(**kwargs)

    


