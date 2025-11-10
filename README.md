# Library Management System

A simple yet powerful Python library management system that handles books, authors, and borrowing records. This system provides a clean API for managing library operations including adding/removing books, tracking borrowings, searching, and generating reports.

## Features

- **Book Management**: Add, remove, and search books with ISBN validation
- **Author Tracking**: Automatic author management when adding books
- **Borrowing System**: Track book borrowings and returns with date management
- **Search Functionality**: Search books by title, author, or ISBN
- **Overdue Detection**: Automatic detection of overdue books with fine calculation
- **Reporting**: Generate library statistics and reports
- **Force Removal**: Handle edge cases with force removal of books

## Installation

### Prerequisites

- Python 3.8 or higher

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install as a Package

```bash
pip install -e .
```

## Quick Start

```python
from library.manager import LibraryManager

# Create a library instance
library = LibraryManager()

# Add books
library.add_book("1984", "George Orwell", "1234567890", 1949)
library.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321", 1960)

# Borrow a book
library.borrow_book("1234567890", "John Doe")

# Search for books
results = library.search_books("Orwell")
for book in results:
    print(f"{book.title} by {book.author}")

# Return a book
library.return_book("1234567890")

# Generate a report
report = library.generate_report()
print(report)
```

## Usage

### Adding Books

```python
# Add a book with basic information
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")

# Add a book with publication year
library.add_book("1984", "George Orwell", "1234567890", 1949)
```

### Borrowing and Returning Books

```python
# Borrow a book
success = library.borrow_book("1234567890", "Alice Johnson")
if success:
    print("Book borrowed successfully!")

# Return a book
success = library.return_book("1234567890")
if success:
    print("Book returned successfully!")
```

### Searching Books

```python
# Search by title
results = library.search_books("1984")

# Search by author
results = library.search_books("George Orwell")

# Search by ISBN
results = library.search_books("1234567890")
```

### Getting Library Information

```python
# Get all available books
available = library.get_available_books()

# Get all borrowed books
borrowed = library.get_borrowed_books()

# Get overdue books
overdue = library.get_overdue_books()

# Get borrowing history for a user
history = library.get_borrowing_history("John Doe")

# Generate a comprehensive report
report = library.generate_report()
# Returns: {
#     "total_books": 10,
#     "available_books": 7,
#     "borrowed_books": 3,
#     "overdue_books": 1
# }
```

### Managing Books

```python
# Remove a book (only if not currently borrowed)
success = library.remove_book("1234567890")

# Force remove a book (even if borrowed, marks as returned)
success = library.force_remove_book("1234567890")

# Check if a book is currently borrowed
is_borrowed = library.is_book_borrowed("1234567890")
```

## API Reference

### LibraryManager

Main class for managing library operations.

#### Methods

- `add_book(title, author_name, isbn, publication_year=None)` - Add a new book to the library
- `remove_book(isbn)` - Remove a book (fails if currently borrowed)
- `force_remove_book(isbn)` - Force remove a book (marks active borrowings as returned)
- `borrow_book(isbn, borrower_name)` - Borrow a book
- `return_book(isbn)` - Return a borrowed book
- `search_books(query)` - Search books by title, author, or ISBN
- `get_available_books()` - Get all available books
- `get_borrowed_books()` - Get all currently borrowed books
- `get_overdue_books()` - Get all overdue borrowing records
- `get_borrowing_history(borrower_name)` - Get borrowing history for a borrower
- `generate_report()` - Generate library statistics report
- `is_book_borrowed(isbn)` - Check if a book is currently borrowed

### Models

#### Book

Represents a book in the library.

**Attributes:**
- `title` (str): Book title
- `author` (str): Author name
- `isbn` (str): ISBN (10 or 13 characters)
- `publication_year` (int, optional): Publication year
- `is_available` (bool): Availability status

#### Author

Represents an author.

**Attributes:**
- `name` (str): Author name
- `birth_year` (int, optional): Birth year
- `nationality` (str, optional): Nationality

#### BorrowingRecord

Represents a borrowing transaction.

**Attributes:**
- `book_isbn` (str): ISBN of the borrowed book
- `borrower_name` (str): Name of the borrower
- `borrow_date` (datetime): Date when book was borrowed
- `return_date` (datetime, optional): Date when book was returned

**Methods:**
- `is_overdue(max_days=14)` - Check if the book is overdue
- `calculate_fine(daily_fine=0.50)` - Calculate fine for overdue books

## Testing

Run the test suite using pytest:

```bash
python -m pytest tests/
```

Run tests with coverage:

```bash
python -m pytest tests/ --cov=library --cov-report=html
```

## Project Structure

```
.
├── library/
│   ├── __init__.py
│   ├── models.py          # Data models (Book, Author, BorrowingRecord)
│   └── manager.py         # LibraryManager class
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   ├── test_models.py     # Tests for models
│   └── test_manager.py    # Tests for LibraryManager
├── example.py             # Example usage script
├── setup.py               # Package setup configuration
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Example Script

Run the example script to see the library in action:

```bash
python example.py
```

Or use the console script (after installation):

```bash
library-demo
```

## Requirements

- Python >= 3.8
- pytest >= 7.0.0 (for testing)
- dataclasses (included in Python 3.7+)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Library System Developer
