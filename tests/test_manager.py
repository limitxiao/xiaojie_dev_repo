"""
Tests for the LibraryManager class.
"""


class TestLibraryManager:
    """Test cases for the LibraryManager class."""
    
    def test_add_book_success(self, library_manager):
        """Test successfully adding a book."""
        result = library_manager.add_book("1984", "George Orwell", "1234567890", 1949)
        assert result is True
        assert "1234567890" in library_manager.books
        assert library_manager.books["1234567890"].title == "1984"
    
    def test_add_duplicate_book(self, library_manager):
        """Test adding a book with duplicate ISBN."""
        library_manager.add_book("1984", "George Orwell", "1234567890", 1949)
        result = library_manager.add_book("Animal Farm", "George Orwell", "1234567890", 1945)
        assert result is False
        assert len(library_manager.books) == 1
    
    def test_add_book_invalid_isbn(self, library_manager):
        """Test adding a book with invalid ISBN."""
        result = library_manager.add_book("Title", "Author", "123")  # Too short
        assert result is False
        assert len(library_manager.books) == 0
    
    def test_remove_book_success(self, populated_library):
        """Test successfully removing a book."""
        result = populated_library.remove_book("1234567890")
        assert result is True
        assert "1234567890" not in populated_library.books
    
    def test_remove_nonexistent_book(self, library_manager):
        """Test removing a book that doesn't exist."""
        result = library_manager.remove_book("9999999999")
        assert result is False
    
    def test_borrow_book_success(self, populated_library):
        """Test successfully borrowing a book."""
        result = populated_library.borrow_book("1234567890", "John Doe")
        assert result is True
        assert not populated_library.books["1234567890"].is_available
        assert len(populated_library.borrowing_records) == 1
    
    def test_borrow_nonexistent_book(self, library_manager):
        """Test borrowing a book that doesn't exist."""
        result = library_manager.borrow_book("9999999999", "John Doe")
        assert result is False
    
    def test_borrow_unavailable_book(self, populated_library):
        """Test borrowing a book that's already borrowed."""
        populated_library.borrow_book("1234567890", "John Doe")
        result = populated_library.borrow_book("1234567890", "Jane Smith")
        assert result is False
        assert len(populated_library.borrowing_records) == 1
    
    def test_return_book_success(self, populated_library):
        """Test successfully returning a book."""
        populated_library.borrow_book("1234567890", "John Doe")
        result = populated_library.return_book("1234567890")
        assert result is True
        assert populated_library.books["1234567890"].is_available
    
    def test_return_nonexistent_book(self, library_manager):
        """Test returning a book that doesn't exist."""
        result = library_manager.return_book("9999999999")
        assert result is False
    
    def test_return_not_borrowed_book(self, populated_library):
        """Test returning a book that wasn't borrowed."""
        result = populated_library.return_book("1234567890")
        assert result is False
    
    def test_search_books_by_title(self, populated_library):
        """Test searching books by title."""
        results = populated_library.search_books("1984")
        assert len(results) == 1
        assert results[0].title == "1984"
    
    def test_search_books_by_author(self, populated_library):
        """Test searching books by author."""
        results = populated_library.search_books("George Orwell")
        assert len(results) == 1
        assert results[0].author == "George Orwell"
    
    def test_search_books_case_insensitive(self, populated_library):
        """Test that search is case insensitive for title and author."""
        results = populated_library.search_books("george orwell")
        assert len(results) == 1
        
        results = populated_library.search_books("MOCKINGBIRD")
        assert len(results) == 1
    
    def test_get_available_books(self, populated_library):
        """Test getting all available books."""
        available = populated_library.get_available_books()
        assert len(available) == 3
        
        populated_library.borrow_book("1234567890", "John Doe")
        available = populated_library.get_available_books()
        assert len(available) == 2
    
    def test_get_borrowed_books(self, populated_library):
        """Test getting all borrowed books."""
        borrowed = populated_library.get_borrowed_books()
        assert len(borrowed) == 0
        
        populated_library.borrow_book("1234567890", "John Doe")
        borrowed = populated_library.get_borrowed_books()
        assert len(borrowed) == 1
    
    def test_get_borrowing_history(self, populated_library):
        """Test getting borrowing history for a user."""
        populated_library.borrow_book("1234567890", "John Doe")
        populated_library.borrow_book("0987654321", "John Doe")
        
        history = populated_library.get_borrowing_history("John Doe")
        assert len(history) == 2
        
        history = populated_library.get_borrowing_history("Jane Smith")
        assert len(history) == 0
    
    def test_generate_report(self, populated_library):
        """Test generating a library report."""
        report = populated_library.generate_report()
        assert report["total_books"] == 3
        assert report["available_books"] == 3
        assert report["borrowed_books"] == 0
        assert report["overdue_books"] == 0
        
        populated_library.borrow_book("1234567890", "John Doe")
        report = populated_library.generate_report()
        assert report["total_books"] == 3
        assert report["available_books"] == 2
        assert report["borrowed_books"] == 1
