"""
Data models for the library management system.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Author:
    """Represents an author."""
    name: str
    birth_year: Optional[int] = None
    nationality: Optional[str] = None
    
    def __post_init__(self):
        if self.birth_year and self.birth_year > datetime.now().year:
            raise ValueError("Birth year cannot be in the future")


@dataclass
class Book:
    """Represents a book in the library."""
    title: str
    author: str
    isbn: str
    publication_year: Optional[int] = None
    is_available: bool = True
    
    def __post_init__(self):
        if len(self.isbn) != 10 and len(self.isbn) != 13:
            raise ValueError("ISBN must be 10 or 13 characters long")
        
        # Bug: This validation is incomplete - it doesn't check for valid ISBN format
        # Missing feature: No genre classification
        # Missing feature: No rating system


@dataclass
class BorrowingRecord:
    """Represents a borrowing transaction."""
    book_isbn: str
    borrower_name: str
    borrow_date: datetime
    return_date: Optional[datetime] = None
    
    def __post_init__(self):
        if self.return_date and self.return_date < self.borrow_date:
            raise ValueError("Return date cannot be before borrow date")
    
    def is_overdue(self, max_days: int = 14) -> bool:
        """Check if the book is overdue."""
        if self.return_date:
            return False
        
        days_borrowed = (datetime.now() - self.borrow_date).days
        return days_borrowed > max_days
    
    def calculate_fine(self, daily_fine: float = 0.50) -> float:
        """Calculate fine for overdue books."""
        if not self.is_overdue():
            return 0.0
        
        # Bug: Calculation doesn't account for weekends or holidays
        overdue_days = (datetime.now() - self.borrow_date).days - 14
        return max(0, overdue_days * daily_fine)
