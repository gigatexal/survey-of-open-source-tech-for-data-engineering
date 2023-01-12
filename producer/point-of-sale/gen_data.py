import random

from typing import Iterable, Generator

from models.models import Book

def pluralize_or_not(word: str)->str:
    if word.endswith("r"):
        return word + 's'
    if word.endswith("d"):
        return word + 's'
    if word.endswith("t"):
        return word + 's'
    if word.endswith("n"):
        return word + 's'
    if word.endswith("c"):
        return word + 's'
    return word


def generate_title_from_noun(source: str, prefix: str = '', pluralize=True)->Generator[str, None, None]:
    with open(source) as nouns:
        all_nouns: list[str] = [w.replace("\n","") for w in nouns.readlines()] 
        while len(all_nouns) > 0:
            choice: str = random.choice(all_nouns) 
            all_nouns.pop(all_nouns.index(choice))
            if pluralize:
                if len(prefix):
                    yield f"{prefix} {pluralize_or_not(choice)}"
                else:
                    yield f"{pluralize_or_not(choice)}"
            elif len(prefix):
                yield f"{prefix} {choice}"
            else:
                yield f"{choice}"



#def create_new_book(subject:str, author: str, price: float, isbn: str, prefix: str ="Everything You Wanted to Know About ", version: int = 1) ->Book:
    
