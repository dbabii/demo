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


def load_books():
    with open("books.json", "r") as f:
        lst = json.load(f)

        for i in lst:
            i = Book(i["title"], i["author"], i["year"])
            library.append(i)


i = 0
menu = ["1. Add book", "2. View book", "3. Save book", "4. Load book"
        , "5. Exit"]

def print_menu():
    for item in menu:
        print(item)


while True:
    print_menu()
    try:
        i = int(input("Please select an option: "))
    except ValueError:
        print("Please enter a digital option")
        continue

    if i == 1:
        print(menu[i-1])
        book = add_book()
        library.append(book)
        print_menu()
    elif i == 2:
        print(menu[i-1])
        view_books()
        print_menu()
    elif i == 3:
        print(menu[i-1])
        save_books()
        print_menu()
    elif i == 4:
        print(menu[i-1])
        load_books()
        print_menu()
    elif i == 5:
        print(menu[i-1])
        break
