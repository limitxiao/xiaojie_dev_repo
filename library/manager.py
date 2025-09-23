"""
Main library management functionality.
"""

from datetime import datetime
from typing import List, Optional, Dict
from .models import Book, Author, BorrowingRecord


class LibraryManager:
    """Main class for managing library operations."""
    
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.authors: Dict[str, Author] = {}
        self.borrowing_records: List[BorrowingRecord] = []
    
    def add_book(self, title: str, author_name: str, isbn: str, 
                 publication_year: Optional[int] = None) -> bool:
        """Add a new book to the library."""
        if isbn in self.books:
            return False
        
        try:
            book = Book(title, author_name, isbn, publication_year)
            self.books[isbn] = book
            
            # Automatically add author if not exists
            if author_name not in self.authors:
                self.authors[author_name] = Author(author_name)
            
            return True
        except ValueError:
            return False
    
    def is_book_borrowed(self, isbn: str) -> bool:
        """Check if a book is currently borrowed."""
        for record in self.borrowing_records:
            if record.book_isbn == isbn and record.return_date is None:
                return True
        return False
    
    def force_remove_book(self, isbn: str) -> bool:
        """Force remove a book from the library, handling active borrowing records."""
        if isbn not in self.books:
            return False
        
        # Mark any active borrowing records as force-returned
        for record in self.borrowing_records:
            if record.book_isbn == isbn and record.return_date is None:
                record.return_date = datetime.now()
        
        del self.books[isbn]
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """Remove a book from the library."""
        if isbn not in self.books:
            return False
        
        # Check if book is currently borrowed
        for record in self.borrowing_records:
            if record.book_isbn == isbn and record.return_date is None:
                return False  # Cannot remove a book that is currently borrowed
        
        del self.books[isbn]
        return True
    
    def borrow_book(self, isbn: str, borrower_name: str) -> bool:
        """Borrow a book from the library."""
        if isbn not in self.books:
            return False
        
        book = self.books[isbn]
        if not book.is_available:
            return False
        
        # Create borrowing record
        record = BorrowingRecord(isbn, borrower_name, datetime.now())
        self.borrowing_records.append(record)
        
        book.is_available = False
        return True
    
    def return_book(self, isbn: str) -> bool:
        """Return a borrowed book."""
        if isbn not in self.books:
            return False
        
        # Find the active borrowing record
        for record in self.borrowing_records:
            if record.book_isbn == isbn and record.return_date is None:
                record.return_date = datetime.now()
                self.books[isbn].is_available = True
                return True
        
        return False
    
    def search_books(self, query: str) -> List[Book]:
        """Search for books by title or author."""
        results = []
        query_lower = query.lower()
        
        for book in self.books.values():
            # Bug: Search is case-sensitive for ISBN
            if (query_lower in book.title.lower() or 
                query_lower in book.author.lower() or
                query in book.isbn):  # This should be case-insensitive too
                results.append(book)
        
        return results
    
    def get_available_books(self) -> List[Book]:
        """Get all available books."""
        return [book for book in self.books.values() if book.is_available]
    
    def get_borrowed_books(self) -> List[Book]:
        """Get all currently borrowed books."""
        return [book for book in self.books.values() if not book.is_available]
    
    def get_overdue_books(self) -> List[BorrowingRecord]:
        """Get all overdue borrowing records."""
        overdue = []
        for record in self.borrowing_records:
            if record.return_date is None and record.is_overdue():
                overdue.append(record)
        return overdue
    
    def get_borrowing_history(self, borrower_name: str) -> List[BorrowingRecord]:
        """Get borrowing history for a specific borrower."""
        return [record for record in self.borrowing_records 
                if record.borrower_name == borrower_name]
    
    def generate_report(self) -> Dict[str, int]:
        """Generate a simple library report."""
        total_books = len(self.books)
        available_books = len(self.get_available_books())
        borrowed_books = len(self.get_borrowed_books())
        overdue_books = len(self.get_overdue_books())
        
        # Missing feature: No statistics about popular books
        # Missing feature: No revenue calculation from fines
        
        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "overdue_books": overdue_books
        }
