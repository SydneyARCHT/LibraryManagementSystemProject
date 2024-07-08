from book import Book
from author import Author
from users import User
from connect_mysql import connect_db
from mysql.connector import Error

class Library:    
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []
    
#----------------------------------------------------------------------------------------------------------
# BOOK FUNCTIONS

    def add_book(self): 
            try:
                conn = connect_db()
                cursor = conn.cursor()

                title = input("Please enter the book's title: ")
                genre = input("Please enter the genre of the book: ")
                publication_date = input("Please enter the date the book was published: ")
                print("Let's get some author details! ")
                author_name = input("Please enter the author's name: ")
                author_bday = input("Please enter the author's birthday: ")
                biography = input("Please enter the author's biography: ")

                author_query = "INSERT INTO authors (name, bday, biography) VALUES (%s, %s, %s)"
                author_data = (author_name, author_bday, biography)
                cursor.execute(author_query, author_data)

                book_query = "INSERT INTO books (title, genre, publication_date) VALUES (%s, %s, %s)"
                book_data = (title, genre, publication_date,)
                cursor.execute(book_query, book_data)
                conn.commit() 
                print()
                print(f"{title} by {author_name} was added to the library!")
                print()
            except Error as e:
                print(f"Error: {e}")

            finally:
                if conn and conn.is_connected():
                    cursor.close()   


    def find_book(self, title):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            query = """
                SELECT b.title, b.genre, b.publication_date, b.availability, a.name
                FROM books b
                JOIN authors a ON b.author_id = a.id
                WHERE b.title = %s
            """
            cursor.execute(query, (title,))
            book = cursor.fetchone()
            if book:
                print("Book found, here is some info: ")
                print(f"Title: {book[0]}")
                print(f"  - Author: {book[4]}")
                print(f"  - Genre: {book[1]}")
                print(f"  - Publication Date: {book[2]}")
                print(f"  - Availability: {book[3]}")
                return book
            else:
                print("Sorry! That book is not in our library.")
                print()
                return None
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    def display_books(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = """
                SELECT b.title, b.genre, b.publication_date, b.availability, a.name
                FROM books b
                JOIN authors a ON b.author_id = a.id
            """
            cursor.execute(query)
            books = cursor.fetchall()
            if books:
                for book in books:
                    print("Book Details: ")
                    print(f"Title: {book[0]}")
                    print(f"  - Author: {book[4]}")
                    print(f"  - Genre: {book[1]}")
                    print(f"  - Publication Date: {book[2]}")
                    print(f"  - Availability: {book[3]}")
                    print()
            else:
                print("No books found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


    def lend_book(self):
        title = input("Which book would you like to borrow? ")
        user_id = int(input("Please enter Library ID: "))
        
        try:
            conn = connect_db()
            cursor = conn.cursor()

            user_query = "SELECT * FROM users WHERE library_id = %s"
            cursor.execute(user_query, (user_id,))
            user = cursor.fetchone()

            if not user:
                print("User not found.")
                return
            book_query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(book_query, (title,))
            book = cursor.fetchone()
            if not book:
                print("Book not found.")
                return
            if book[4] == "Available":
                update_query = "UPDATE books SET availability = 'Borrowed' WHERE id = %s"
                cursor.execute(update_query, (book[0],))
                lending_query = "INSERT INTO lendings (user_id, book_id) VALUES (%s, %s)"
                cursor.execute(lending_query, (user[0], book[0]))

                conn.commit()
                print(f"{title} has been rented out by {user[1]}")
            else:
                print(f"Book '{title}' is not available for borrowing.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    def return_book(self):
        title = input("Which book would you like to return? ")
        try:
            conn = connect_db()
            cursor = conn.cursor()
            book_query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(book_query, (title,))
            book = cursor.fetchone()
            if not book:
                print("Book not found.")
                return

            if book[4] == "Borrowed":
                update_query = "UPDATE books SET availability = 'Available' WHERE id = %s"
                cursor.execute(update_query, (book[0],))
                delete_query = "DELETE FROM lendings WHERE book_id = %s"
                cursor.execute(delete_query, (book[0],))

                conn.commit()
                print(f"Book '{title}' has been returned.")
            else:
                print(f"Book '{title}' is not borrowed.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

#----------------------------------------------------------------------------------------------------------
# USER FUNCTIONS         
    
    def add_user(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            name = input("Please enter new user name: ")
            email = input("Please enter a new email: ")
            library_id = int(input("Please enter a new library ID: "))
            query = "INSERT INTO users (name, email, library_id) VALUES (%s, %s, %s)"
            user_data = (name, email, library_id)
            cursor.execute(query, user_data)
            conn.commit() 
            print(f"{name} has been added with library ID {library_id}")
            print()
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()   

    def find_user(self):
        name = input("Who is the user you are looking for? ")
        try:
            conn = connect_db()
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE name = %s"
            cursor.execute(query, (name,))
            user = cursor.fetchone()
            if user:
                print("User found, here is some info:")
                print(f"Name: {user[1]}")
                print(f"- Email: {user[2]}")
                print(f"- Library ID: {user[3]}")
            print(f"User '{name}' not found.")
            return None
        except Error as e:
            print(f"Error occurred: {e}")
            return None
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def display_users(self):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()

        if users:
            for user in users:
                print("User found, here is some info:")
                print(f"Name: {user[1]}")
                print(f"- Email: {user[2]}")
                print(f"- Library ID: {user[3]}")
                print() 
        else:
            print("No users found.")

    except Error as e:
        print(f"Error occurred: {e}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

#----------------------------------------------------------------------------------------------------------
# AUTHOR FUNCTIONS 

    def add_author(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            author_name = input("Please enter the author's name: ")
            author_bday = input("Please enter the author's birthday: ")
            biography = input("Please enter the author's biography: ")

            author_query = "INSERT INTO authors (name, bday, biography) VALUES (%s, %s, %s)"
            author_data = (author_name, author_bday, biography)
            cursor.execute(author_query, author_data)
            conn.commit() 
            print()
            print(f"{author_name} was added to the author section")
            print()
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()   



    def find_author(self):
        name = input("Who is the author you are looking for? ")
        try:
            conn = connect_db()
            cursor = conn.cursor()

            query = "SELECT * FROM authors WHERE name = %s"
            cursor.execute(query, (name,))
            author = cursor.fetchone() 
            if author:
                print(f"Author found: {author[1]}")
                print(f"- Birthday: {author[2]}")
                print(f"- Biography: {author[3]}")
                return author
            else:
                print(f"Author '{name}' not found.")
                return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


    def view_authors(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()

            query = "SELECT * FROM authors"
            cursor.execute(query)
            authors = cursor.fetchall()

            if not authors:
                print("No authors found.")
            else:
                for author in authors:
                    print(f"Author: {author[1]}")
                    print(f"- Birthday: {author[2]}")
                    print(f"- Biography: {author[3]}")
                    print()  
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

#----------------------------------------------------------------------------------------------------------
    