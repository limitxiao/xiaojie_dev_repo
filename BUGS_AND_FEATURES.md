# Library Management System - Known Issues and Missing Features

This document describes the intentional bugs and missing features in the Library Management System that can be addressed by future development or bug fixes.

## Intentional Bugs

### 1. Book Removal Without Checking Borrowing Status
**Location**: `library/manager.py`, `remove_book()` method  
**Issue**: The system allows removing books that are currently borrowed without checking if they have active borrowing records.  
**Expected Behavior**: Should prevent removal of borrowed books or handle the borrowing records appropriately.

### 2. Case-Sensitive ISBN Search
**Location**: `library/manager.py`, `search_books()` method  
**Issue**: While title and author searches are case-insensitive, ISBN search is case-sensitive.  
**Expected Behavior**: All search fields should be consistently case-insensitive.

### 3. Incomplete ISBN Validation
**Location**: `library/models.py`, `Book.__post_init__()` method  
**Issue**: Only validates ISBN length (10 or 13 characters) but doesn't check for valid ISBN format or checksums.  
**Expected Behavior**: Should validate ISBN-10 and ISBN-13 checksums and format.

### 4. Fine Calculation Doesn't Account for Weekends/Holidays
**Location**: `library/models.py`, `BorrowingRecord.calculate_fine()` method  
**Issue**: Fine calculation assumes every day is a business day.  
**Expected Behavior**: Should exclude weekends and holidays from fine calculations.

## Missing Features

### 1. Genre Classification System
**Description**: Books currently don't have genre/category classification.  
**Suggested Implementation**: 
- Add `genre` field to `Book` model
- Add genre-based search functionality
- Add genre statistics to reports

### 2. Book Rating System
**Description**: No mechanism to rate or review books.  
**Suggested Implementation**:
- Add `Rating` model with user ratings
- Add average rating calculation
- Add rating-based book recommendations

### 3. Popular Books Statistics
**Description**: Reports don't include information about most borrowed or popular books.  
**Suggested Implementation**:
- Track borrowing frequency
- Add popular books section to reports
- Add trending books functionality

### 4. Revenue Calculation from Fines
**Description**: System tracks fines but doesn't calculate total revenue.  
**Suggested Implementation**:
- Add revenue tracking in reports
- Add fine payment tracking
- Add financial summaries

### 5. Advanced Search Features
**Description**: Search is basic and doesn't support advanced queries.  
**Suggested Implementation**:
- Add filters for publication year, genre, availability
- Add sorting options
- Add fuzzy search capabilities

### 6. User Management System
**Description**: Currently only tracks borrower names as strings.  
**Suggested Implementation**:
- Add `User` model with contact information
- Add user borrowing limits
- Add user preference tracking

### 7. Reservation System
**Description**: No way to reserve books that are currently borrowed.  
**Suggested Implementation**:
- Add `Reservation` model
- Add queue management for popular books
- Add notification system for available books

## Test Coverage Notes

The current test suite covers:
- ✅ Basic CRUD operations for all models
- ✅ Error handling for invalid inputs
- ✅ Business logic validation
- ✅ Search functionality
- ✅ Borrowing and returning workflows

### Safe Test Extension Guidelines

When adding new test cases:

1. **Import Structure**: All necessary imports are already available through the `conftest.py` fixtures
2. **Test Isolation**: Each test uses fresh fixtures, so new tests won't interfere with existing ones
3. **Model Extensions**: New models can be imported in individual test files without breaking existing tests
4. **Manager Extensions**: New methods on `LibraryManager` can be tested independently

### Example of Safe Test Addition

```python
# New test file: tests/test_new_feature.py
"""
Tests for new features.
"""

def test_new_feature(library_manager):
    """Test new functionality."""
    # This will not break existing tests
    # even if the new feature doesn't exist yet
    try:
        result = library_manager.new_method()
        assert result is not None
    except AttributeError:
        # Method doesn't exist yet - test will fail but not crash
        assert False, "new_method not implemented"
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_models.py -v

# Run with coverage
python -m pytest tests/ --cov=library
```
