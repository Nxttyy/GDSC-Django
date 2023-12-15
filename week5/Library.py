import json

class Library(object):
    """docstring for Library."""
    users = []
    books = []
    transactions = []

    def add_book(**kwargs):
        if kwargs:
            Library.books.append(Book(kwargs["title"], kwargs["author"]
                                        , kwargs["isbn"], kwargs["available"]))

        else:
            title = input("What is the title?")
            author = input("who is the author?")
            isbn = input("What is the ISBN?")

            Library.books.append(Book(title, author, isbn, True))



    def list_books():
        for book in Library.books:
            print(f"id. :{Library.books.index(book)}, title: {book.title}")

    def register_user():
        name = input("What is your name?")
        user = User(name)
        Library.users.append(user)

        name, _id = user.user_details()
        print(f"Account created for {name}, with id no. {_id}")

    def borrow_book():
        user_id = int(input("What is your id number?"))
        for u in Library.users:
            if user_id == u.user_id:
                user = u


        book_id = int(input("what is the id. number of the book you want to borrow?"))
        book = Library.books[book_id]

        try:
            Library.transactions.append(Transactions.borrowing(user, book))
        except UnboundLocalError:
            print("No user with this id found")

    def return_book():
        user_id = int(input("What is your id number?"))
        for u in Library.users:
            if user_id == u.user_id:
                user = u


        book_id = int(input("what is the id. number of the book you are returning?"))
        book = Library.books[book_id]

        try:
            Library.transactions.append(Transactions.returning(user, book))
        except UnboundLocalError:
            print("No user with this id found")


class Book(object):
    """docstring for Book."""

    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available


    def book_details(self):
        return self.title, self.author

    def update_availablity(self, status):
        self.available = status


class User(object):
    """docstring for User"""

    user_id = 0


    def __init__(self, name, books_borrowed=[]):
        self.name = name
        self.user_id = User.user_id
        self.books_borrowed = books_borrowed

        User.user_id += 1


    def user_details(self):
        return self.name, self.user_id

    def borrow_book(self, book):
        self.books_borrowed.append(book)

    def return_book(self, book):
        self.books_borrowed.remove(book)


class Transactions(object):
    """docstring for Transactions."""

    def borrowing(user, book):
        Library.transactions.append(f"{user.name} borrowed {book.isbn}")
        user.borrow_book(book)
        book.update_availablity(False)

    def returning(user, book):
        Library.transactions.append(f"{user.name} returned {book.isbn}")
        user.return_book(book)
        book.update_availablity(True)

#Load the dummy data for pre-added books
json_file = open("./dummy_books.json")
books = json.load(json_file)["books"]

#preload the dummy books from the json data
for book in books:
    Library.add_book(title=book["title"], author=book["author"], isbn=book["isbn"], available=True)

#Looping choice menu
exit = False
while not exit:
    try:
        choice = int(input("""Please enter your choice:
                            1. Register user.
                            2. Add book.
                            3. List Books.
                            4. Borrow a book.
                            5. Return a Book.
                            6. EXIT"""))
    except ValueError:
        print("Please enter from the given choices only.")

    else:
        if choice == 1:
            Library.register_user()

        elif choice == 2:
            Library.add_book()

        elif choice == 3:
            Library.list_books()

        elif choice == 4:
            Library.borrow_book()
        elif choice == 5:
            Library.return_book()
        elif choice == 6:
            exit = True

        else:
            print("invalid input")
