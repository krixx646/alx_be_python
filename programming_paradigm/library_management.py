# library_management.py

class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private by convention

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book with the given title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book with the given title to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' is not checked out.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(book)
