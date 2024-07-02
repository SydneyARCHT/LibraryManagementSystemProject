from library import Library
    
def enter_book_operations(library):
    while True:
        print("""Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books
        6. Back to Main Menu 
                         """)
        response = input("Please enter another choice: ")
        if response == "1":
            print()
            library.add_book()
        elif response == "2":
            print()
            library.lend_book()
        elif response == "3":
            print()
            library.return_book()
        elif response == "4":
            print()
            title = input("What book are you looking for? ")
            library.find_book(title)
        elif response == "5":
            print()
            library.display_books()
        elif response == "6":
            break


def enter_user_operations(library):
    while True:
        print("""User Operations:
        1. Add a new user
        2. View user details
        3. Display all users
        4. Back to Main Menu
        """)
        response = input("Please enter your choice: ")
        if response == "1":
            print()
            library.add_user()
        elif response == "2":
            print()
            library.find_user()
        elif response == "3":
            print()
            library.display_users()
        elif response == "4":
            break
        else:
            print("Please enter a valid choice.")



def enter_author_operations(library):
    while True:
        print("""Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors
        4. Back to Main Menu
        """)
        response = input("Please enter your choice: ")
        if response == "1":
            print()
            library.add_author()
        elif response == "2":
            print()
            library.find_author()
        elif response == "3":
            print()
            library.view_authors()
        elif response == "4":
            break
        else:
            print("Please enter a valid choice.")


def main():
    library = Library()
    while True:
        print("""
              1. Book Operations
              2. User Operations
              3. Author Operations
              4. Exit""")
        print()
        response = input("Enter your choice: ")
        if response == "1":
            print()
            enter_book_operations(library)
        elif response == "2":
            print()
            enter_user_operations(library)
        elif response == "3":
            print()
            enter_author_operations(library)
        elif response == "4":
            print()
            print("Exiting Program... ")
            break
        else:
            print("Please enter a valid choice... ")

main()