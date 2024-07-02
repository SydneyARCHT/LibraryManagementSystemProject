
class User:
    def __init__(self, name, email, library_id):
        self.__name = name
        self.__email = email
        self.__library_id = library_id
        self.borrowed_books = []

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, new_id):
        self.__library_id = new_id

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, title):
        for book in self.borrowed_books:
            if title == book.get_title():
                self.borrowed_books.remove(book)
                print(self.borrowed_books)



    
