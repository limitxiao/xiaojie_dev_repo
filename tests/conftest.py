"""
Test configuration and fixtures.
"""

import pytest
from library.manager import LibraryManager


@pytest.fixture
def library_manager():
    """Create a fresh LibraryManager instance for testing."""
    return LibraryManager()


@pytest.fixture
def sample_books():
    """Sample books for testing."""
    return [
        {"title": "1984", "author": "George Orwell", "isbn": "1234567890", "year": 1949},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "0987654321", "year": 1960},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "1122334455", "year": 1925}
    ]


@pytest.fixture
def populated_library(library_manager, sample_books):
    """Create a library manager with sample books."""
    for book in sample_books:
        library_manager.add_book(
            book["title"], 
            book["author"], 
            book["isbn"], 
            book["year"]
        )
    return library_manager
