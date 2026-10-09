myBookList = []
myAuthorList = []
myUserList = []

class Book_class:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""

    def add_book(self):
        self.book_id = input("Enter book ID: ")
        self.book_title = input("Enter book title: ")
        self.author_id = input("Enter author ID: ")
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = input("Enter year of publication: ")

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Book title:", self.book_title)
        print("Author ID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year of publication:", self.year_of_publication)

class Author_class:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailid = ""

    def add_author(self):
        self.author_id = input("Enter author ID: ")
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone: ")
        self.emailid = input("Enter email ID: ")

    def display_author(self):
        print("Author ID:", self.author_id)
        print("Author name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email ID:", self.emailid)

class User_class:
    def __init__(self):
        self.user_id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailid = ""
        self.booksborrowed = []

    def add_user(self):
        self.user_id = input("Enter user ID: ")
        self.name = input("Enter user name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone: ")
        self.emailid = input("Enter email ID: ")

    def display_user(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Password:", self.password)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email ID:", self.emailid)
        print("Books borrowed:", self.booksborrowed)

# Main Program

choice = ""

while choice != "0":
    print()
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1. Add books")
    print("2. Add authors")
    print("3. Add users")
    print("4. Display all records")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        numBooks = int(input("How many books do you want to create? "))

        for i in range(numBooks):
            book = Book_class()
            book.add_book()
            myBookList.append(book)

    elif choice == "2":
        numAuthors = int(input("How many authors do you want to create? "))

        for i in range(numAuthors):
            author = Author_class()
            author.add_author()
            myAuthorList.append(author)

    elif choice == "3":
        numUsers = int(input("How many users do you want to create? "))

        for i in range(numUsers):
            user = User_class()
            user.add_user()
            myUserList.append(user)

    elif choice == "4":
        print()
        print("BOOK LIST")

        for book in myBookList:
            book.display_book()
            print()

        print("AUTHOR LIST")

        for author in myAuthorList:
            author.display_author()
            print()

        print("USER LIST")

        for user in myUserList:
            user.display_user()
            print()

    elif choice == "5":
        print("Exit")

    else:
        print("Invalid choice.")