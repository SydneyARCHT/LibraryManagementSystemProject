

class Author:
    def __init__(self, name, bday, biography):
        self.__name = name
        self.__bday = bday
        self.__biography = biography

    def get_author_name(self):
        return self.__name
    
    def set_author_name(self, new_author_name):
        self.__name = new_author_name

    def get_bday(self):
        return self.__bday
    
    def set_bday(self, new_bday):
        self.__bday = new_bday

    def get_bio(self):
        return self.__biography
    
    def set_bio(self, new_bio):
        self.__biography = new_bio

    