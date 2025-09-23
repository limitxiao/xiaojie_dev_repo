"""
Library Management System
A simple system to manage books, authors, and borrowing records.
"""

from .manager import LibraryManager
from .models import Book, Author, BorrowingRecord

__version__ = "1.0.0"
__all__ = ["LibraryManager", "Book", "Author", "BorrowingRecord"]
