#       Class Methods
#       Task:
# Create a class Book with a class variable total_books.
#  Add a class method increment_book_count() to increase the count when a new book is added.

from typing import NoReturn

class Book:
    total_books : int = 0

    @classmethod 
    def increment_book_count(cls)->NoReturn:
        cls.total_books += 1
    
print("Total Books: "+str(Book.total_books))
Book.increment_book_count()
print("Total Books: "+str(Book.total_books))