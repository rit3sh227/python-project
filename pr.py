# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Book Class
class Book:
    def _init_(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.is_issued = False

    def _str_(self):
        return f"{self.book_id}: {self.title} by {self.author} (Genre: {self.genre}) {'[Issued]' if self.is_issued else ''}"

# User Class
class User:
    def _init_(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def _str_(self):
        return f"User {self.user_id}: {self.name} | Borrowed Books: {len(self.borrowed_books)}"

# Library Management System Class
class Library:
    def _init_(self):
        self.books = []
        self.users = {}
        self.history = []

    # Add Book
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter book genre: ")
        book_id = len(self.books) + 1
        new_book = Book(title, author, genre, book_id)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    # View All Books
    def view_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    # Search Book
    def search_book(self):
        search_query = input("Enter book title or author to search: ").lower()
        results = [book for book in self.books if search_query in book.title.lower() or search_query in book.author.lower()]
        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        else:
            print("No books found matching the query.")

    # Add User
    def add_user(self):
        name = input("Enter user name: ")
        user_id = len(self.users) + 1
        new_user = User(name, user_id)
        self.users[user_id] = new_user
        print(f"User '{name}' added successfully with User ID {user_id}!")

    # Issue Book
    def issue_book(self):
        user_id = int(input("Enter user ID: "))
        if user_id not in self.users:
            print("User not found!")
            return
        user = self.users[user_id]
        book_id = int(input("Enter book ID to issue: "))
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print(f"Book '{book.title}' is already issued.")
                else:
                    book.is_issued = True
                    user.borrowed_books.append(book)
                    self.history.append((user.name, book.title, "Issued", datetime.now()))
                    print(f"Book '{book.title}' issued to {user.name}.")
                return
        print("Book not found!")

    # Return Book
    def return_book(self):
        user_id = int(input("Enter user ID: "))
        if user_id not in self.users:
            print("User not found!")
            return
        user = self.users[user_id]
        book_id = int(input("Enter book ID to return: "))
        for book in user.borrowed_books:
            if book.book_id == book_id:
                book.is_issued = False
                user.borrowed_books.remove(book)
                self.history.append((user.name, book.title, "Returned", datetime.now()))
                print(f"Book '{book.title}' returned by {user.name}.")
                return
        print("Book not found in user's borrowed list!")

    # View History
    def view_history(self):
        if not self.history:
            print("No history available.")
        else:
            print("\nTransaction History:")
            for record in self.history:
                print(f"{record[0]} {record[2]} '{record[1]}' on {record[3].strftime('%Y-%m-%d %H:%M:%S')}")

    # Visualize Genres
    def visualize_genres(self):
        genres = [book.genre for book in self.books]
        genre_counts = {genre: genres.count(genre) for genre in set(genres)}
        plt.bar(genre_counts.keys(), genre_counts.values(), color='skyblue')
        plt.title("Popular Book Genres")
        plt.xlabel("Genre")
        plt.ylabel("Count")
        plt.show()

    # Main Menu
    def menu(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Search Book")
            print("4. Add User")
            print("5. Issue Book")
            print("6. Return Book")
            print("7. View History")
            print("8. Visualize Genres")
            print("9. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.add_user()
            elif choice == '5':
                self.issue_book()
            elif choice == '6':
                self.return_book()
            elif choice == '7':
                self.view_history()
            elif choice == '8':
                self.visualize_genres()
            elif choice == '9':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

# Run the Library Management System
if _name_ == "_main_":
    library = Library()
    library.menu()
