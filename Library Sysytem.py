class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0
        print("Welcome to the Library Management System")
        print("You can add, remove, and view books in the library.")
        no_of_books = int(input("Enter the number of books you want to add: "))
        for i in range(no_of_books):
            book_name = input(f"Enter the name of book {i + 1}: ")
            self.books.append(book_name)
            self.no_of_books += 1
        print(f"{self.no_of_books} books have been added to the library.")
        print("Here are the books in the library:")
        for book in self.books:
            print(book)
        print(f"Total no. of books before are {self.no_of_books}")
        self.before_books = self.no_of_books  
        # Save the initial number of books
        borrow_choice = input("Do you want to borrow a book? (yes/no):\n").strip().lower()
        if borrow_choice == 'yes':
            self.borrow_book()
        elif borrow_choice == 'no':
            print("Thank you for using the Library Management System.")
            exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    def borrow_book(self):
        book_name = input("Enter the name of the book you want to borrow: ")
        if book_name in self.books:
            self.books.remove(book_name)
            self.no_of_books -= 1
            print(f"You have borrowed '{book_name}'.")
            print(f"Books left in the library: {self.no_of_books}")
        else:
            print(f"Sorry, '{book_name}' is not available in the library.")
        print(f"Total no. of books after are {self.no_of_books}")
        # Call the static method to compare
        Library.compare_books(self.before_books, self.no_of_books)

    @staticmethod
    def compare_books(before, after):
        if before == after:
            print("The number of books before and after is equal.")
        else:
            print("The number of books before and after is NOT equal.")

Library()
compare_books = Library.compare_books
