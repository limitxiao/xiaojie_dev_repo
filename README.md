# Library Management System

A simple Python library management system that handles books, authors, and borrowing records.

## Features

- Add and manage books
- Track authors
- Record borrowing transactions
- Search functionality
- Generate reports

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from library.manager import LibraryManager

# Create a library instance
library = LibraryManager()

# Add books
library.add_book("1984", "George Orwell", "123456789")

# Borrow a book
library.borrow_book("123456", "John Doe")
```

## Testing

```bash
python -m pytest tests/
```
