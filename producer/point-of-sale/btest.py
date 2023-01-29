from service.newbook import isbn, author, title, price, new_book

if __name__ == '__main__':
    d = [
            {'isbn':isbn(),
             'author': author(),
             'title': title(),
             'price': price()
             }
            for _ in range(100)]
    print(len(d), len(set([tuple(x.values()) for x in d])))
    x = new_book(title=title(), author=author(), price=price(), isbn=isbn())
    print(f"book x is {x}")
    y = new_book(title=title(), author=author(), price=price(), isbn=isbn())
    print(f"book y is {y}")
