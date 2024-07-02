

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self._publication_date = publication_date
        self.__is_available = True 

    def get_title(self):
        return self.__title

    def get_availability(self):
        if self.__is_available:
            return "Available"
        else:
            return "Borrowed"

    def set_availability(self):
        if self.get_availability():
            self.__is_available = False
        else:
            self.__is_available = True

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self._publication_date

    def borrow_book(self):
        if self.get_availability():
            self.set_availability()
            return True 
        return False
    
    def return_book(self):
        self.set_availability()

