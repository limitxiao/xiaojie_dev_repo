"""
Tests for the Book, Author, and BorrowingRecord models.
"""

import pytest
from datetime import datetime, timedelta
from library.models import Book, Author, BorrowingRecord


class TestAuthor:
    """Test cases for the Author model."""
    
    def test_create_author_basic(self):
        """Test creating an author with just a name."""
        author = Author("George Orwell")
        assert author.name == "George Orwell"
        assert author.birth_year is None
        assert author.nationality is None
    
    def test_create_author_full(self):
        """Test creating an author with all details."""
        author = Author("George Orwell", 1903, "British")
        assert author.name == "George Orwell"
        assert author.birth_year == 1903
        assert author.nationality == "British"
    
    def test_author_future_birth_year(self):
        """Test that future birth year raises an error."""
        with pytest.raises(ValueError, match="Birth year cannot be in the future"):
            Author("Future Author", 2030)


class TestBook:
    """Test cases for the Book model."""
    
    def test_create_book_basic(self):
        """Test creating a book with basic information."""
        book = Book("1984", "George Orwell", "1234567890")
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.isbn == "1234567890"
        assert book.is_available is True
    
    def test_create_book_with_year(self):
        """Test creating a book with publication year."""
        book = Book("1984", "George Orwell", "1234567890", 1949)
        assert book.publication_year == 1949
    
    def test_invalid_isbn_length(self):
        """Test that invalid ISBN length raises an error."""
        with pytest.raises(ValueError, match="ISBN must be 10 or 13 characters long"):
            Book("Title", "Author", "123")
        
        with pytest.raises(ValueError, match="ISBN must be 10 or 13 characters long"):
            Book("Title", "Author", "12345678901234")


class TestBorrowingRecord:
    """Test cases for the BorrowingRecord model."""
    
    def test_create_borrowing_record(self):
        """Test creating a borrowing record."""
        borrow_date = datetime.now()
        record = BorrowingRecord("1234567890", "John Doe", borrow_date)
        assert record.book_isbn == "1234567890"
        assert record.borrower_name == "John Doe"
        assert record.borrow_date == borrow_date
        assert record.return_date is None
    
    def test_invalid_return_date(self):
        """Test that return date before borrow date raises an error."""
        borrow_date = datetime.now()
        return_date = borrow_date - timedelta(days=1)
        
        with pytest.raises(ValueError, match="Return date cannot be before borrow date"):
            BorrowingRecord("1234567890", "John Doe", borrow_date, return_date)
    
    def test_is_overdue_not_returned(self):
        """Test overdue detection for unreturned books."""
        # Book borrowed 20 days ago
        borrow_date = datetime.now() - timedelta(days=20)
        record = BorrowingRecord("1234567890", "John Doe", borrow_date)
        assert record.is_overdue() is True
    
    def test_is_not_overdue_recent(self):
        """Test that recently borrowed books are not overdue."""
        # Book borrowed 5 days ago
        borrow_date = datetime.now() - timedelta(days=5)
        record = BorrowingRecord("1234567890", "John Doe", borrow_date)
        assert record.is_overdue() is False
    
    def test_is_not_overdue_returned(self):
        """Test that returned books are not overdue."""
        # Book borrowed 20 days ago but returned
        borrow_date = datetime.now() - timedelta(days=20)
        return_date = datetime.now() - timedelta(days=1)
        record = BorrowingRecord("1234567890", "John Doe", borrow_date, return_date)
        assert record.is_overdue() is False
    
    def test_calculate_fine_no_fine(self):
        """Test fine calculation for non-overdue books."""
        borrow_date = datetime.now() - timedelta(days=5)
        record = BorrowingRecord("1234567890", "John Doe", borrow_date)
        assert record.calculate_fine() == 0.0
    
    def test_calculate_fine_overdue(self):
        """Test fine calculation for overdue books."""
        # Book borrowed 20 days ago (6 days overdue)
        borrow_date = datetime.now() - timedelta(days=20)
        record = BorrowingRecord("1234567890", "John Doe", borrow_date)
        expected_fine = 6 * 0.50  # 6 overdue days * $0.50 per day
        assert record.calculate_fine() == expected_fine
