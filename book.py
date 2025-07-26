import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"The title of the books is {self.title}")
        print(f"The author is {self.author}")
        print(f"The book was published in {self.year}")


library = []

def add_book():
    title = input("Please enter a title: ")
    author = input("Please enter an author: ")
    year = int(input("Please enter a year: "))
    
    book = Book(title, author, year)
    return book

def view_books():
    if len(library) == 0:
        print("Library is empty")
    else:
        for i in library:
            i.describe()

def save_books():
    data = []
    for i in library:
        data.append({"title": i.title,
                     "author": i.author,
                     "year": i.year})
    with open("books.json", "w") as file:
        json.dump(data, file)
