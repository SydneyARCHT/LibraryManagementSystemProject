from book import Book
from author import Author
from users import User
class Library:    
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []
    
#----------------------------------------------------------------------------------------------------------
# BOOK FUNCTIONS

    def add_book(self): 
            title = input("Please enter the book's title: ")
            genre = input("Please enter the genre of the book: ")
            publication_date = input("Please enter the date the book was published: ")
            print("Let's get some author details! ")
            author_name = input("Please enter the author's name: ")
            author_bday = input("Please enter the author's birthday: ")
            author_bio = input("Please enter the author's biography: ")
            author = Author(author_name, author_bday, author_bio)
            self.authors.append(author)  
            book = Book(title, author, genre, publication_date)
            self.books.append(book)
            print()
            print(f"{title} by {author_name} was added to the library!")
            print()

    def find_book(self, title):
        try:
            for book in self.books:
                if book.get_title() == title:
                    print("Book found, here is some info: ")
                    print(f"{book.get_title()}")
                    print(f"  - {book.get_author().get_author_name()}")
                    print(f"  - {book.get_genre()}")
                    print(f"  - {book.get_publication_date()}")
                    print(f"  - {book.get_availability()}")
                    return book
        except:
            print("Sorry! That book is not in our library. ")
            print()
    
    def display_books(self):
        for book in self.books:
            print("Book Details: ")
            print(f"{book.get_title()}")
            print(f"  - {book.get_author().get_author_name()}")
            print(f"  - {book.get_genre()}")
            print(f"  - {book.get_publication_date()}")
            print(f"  - {book.get_availability()}")
            print()


    def lend_book(self):
        title = input("Which book would you like to borrow? ")
        user_id = int(input("Please enter Library ID: "))
        self.current_user = None
        self.current_book = None
        for users in self.users:
            if user_id == users.get_library_id():
                self.current_user = users
        for book in self.books:
            if title == book.get_title():
                self.current_book = book
        if self.current_user and self.current_book:
            if book.get_availability() == "Available":
                self.current_user.borrow_book(self.current_book)
                self.current_book.borrow_book()
                print(f"{title} has been rented out by {self.current_user.get_name()}")
            else:
                print(f"Book '{book.get_title()}' is not available for borrowing.")
        else:
            print(f"Book '{title}' is not in our library.")

    def return_book(self):
        title = input("Which book would you like to return? ")
        book = self.find_book(title)
        if book:
            if book.get_availability() == "Borrowed":
                book.set_availability()
                for user in self.users:
                    for book in user.borrowed_books:
                        if title == book.get_title():
                            user.borrowed_books.remove(book)
                    print(user.borrowed_books)
                print(f"Book '{book.get_title()}' has been returned.")
            else:
                print(f"Book '{book.get_title()}' is not borrowed.")
        else:
            print(f"Book '{title}' is not in our library.")

#----------------------------------------------------------------------------------------------------------
# USER FUNCTIONS         
    
    def add_user(self):
        name = input("Please enter new user name: ")
        email = input("Please enter a new email: ")
        library_id = int(input("Please enter a new library ID: "))
        user = User(name, email, library_id)
        self.users.append(user)
        print(f"{name} has been added with library ID {library_id}")
        print()

    def find_user(self):
        name = input("Who is the user you are looking for? ")
        try:
            for user in self.users:
                if user.get_name() == name:
                    print("User found, here is some info: ")
                    print(f"{user.get_name()}")
                    print(f"-  Email: {user.get_email()}")
                    print(f"-  Library ID: {user.get_library_id()}")
                    print(f"-  Borrored Books: {', '.join(user.borrowed_books)}" if user.borrowed_books else "-  No Books Borrowed")
                    return user
        except:
            print("Error has occured, please enter a valid user... ")

    def display_users(self):
        for user in self.users:
            print("User found, here is some info: ")
            print(f"{user.get_name()}")
            print(f"-  Email: {user.get_email()}")
            print(f"-  Library ID: {user.get_library_id()}")
            print(f"-  Borrored Books: {', '.join(user.borrowed_books)}" if user.borrowed_books else "-  No Books Borrowed")

#----------------------------------------------------------------------------------------------------------
# AUTHOR FUNCTIONS 

    def add_author(self):
        name = input("Name of Author: ")
        bday = input("Author Birthday: ")
        bio = input("Author Bio: ")
        author = Author(name, bday, bio)
        self.authors.append(author)

    def find_author(self):
        name = input("Who is the author you are looking for? ")
        try:
            for author in self.authors:
                if author.get_author_name() == name:
                    print(f"Author found: {author.get_author_name()}")
                    print(f"- Birthday: {author.get_bday()}")
                    print(f"- Biography: {author.get_bio()}")
                    return author
        except:
            print("Error has occured, please enter a valid author... ")


    def view_authors(self):
        for author in self.authors:
            print(f"Author found: {author.get_author_name()}")
            print(f"- Birthday: {author.get_bday()}")
            print(f"- Biography: {author.get_bio()}")

#----------------------------------------------------------------------------------------------------------
    

# Lend and return are the only one that needs arguments???