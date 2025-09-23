#!/usr/bin/env python3
"""
Demonstration of the book removal bug fix.

This script shows that:
1. Books can be removed when they are not borrowed
2. Books cannot be removed when they are currently borrowed
3. Books can be removed after they are returned
4. Force removal is available for administrative purposes
"""

from library.manager import LibraryManager


def main():
    # Create a library and add some books
    library = LibraryManager()
    
    print("=== Library Book Removal Bug Fix Demo ===\n")
    
    # Add some books
    library.add_book("1984", "George Orwell", "1234567890", 1949)
    library.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321", 1960)
    
    print("1. Added books to the library:")
    for isbn, book in library.books.items():
        print(f"   - {book.title} by {book.author} (ISBN: {isbn})")
    
    print(f"\nTotal books: {len(library.books)}")
    
    # Test 1: Remove a book that's not borrowed (should succeed)
    print("\n2. Attempting to remove '1984' (not borrowed)...")
    result = library.remove_book("1234567890")
    print(f"   Result: {'SUCCESS' if result else 'FAILED'}")
    print(f"   Books remaining: {len(library.books)}")
    
    # Add the book back for further testing
    library.add_book("1984", "George Orwell", "1234567890", 1949)
    
    # Test 2: Borrow a book and try to remove it (should fail)
    print("\n3. Borrowing 'To Kill a Mockingbird' and attempting to remove it...")
    library.borrow_book("0987654321", "John Doe")
    print("   Book borrowed by John Doe")
    print(f"   Is book borrowed? {library.is_book_borrowed('0987654321')}")
    
    result = library.remove_book("0987654321")
    print(f"   Removal attempt result: {'SUCCESS' if result else 'FAILED'}")
    print(f"   Books remaining: {len(library.books)}")
    
    # Test 3: Return the book and try to remove it (should succeed)
    print("\n4. Returning the book and attempting to remove it...")
    library.return_book("0987654321")
    print("   Book returned")
    print(f"   Is book still borrowed? {library.is_book_borrowed('0987654321')}")
    
    result = library.remove_book("0987654321")
    print(f"   Removal attempt result: {'SUCCESS' if result else 'FAILED'}")
    print(f"   Books remaining: {len(library.books)}")
    
    # Test 4: Force removal demonstration
    print("\n5. Demonstrating force removal for administrative purposes...")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455", 1925)
    library.borrow_book("1122334455", "Jane Smith")
    print("   'The Great Gatsby' borrowed by Jane Smith")
    print(f"   Is book borrowed? {library.is_book_borrowed('1122334455')}")
    
    print("   Regular removal attempt...")
    result = library.remove_book("1122334455")
    print(f"   Result: {'SUCCESS' if result else 'FAILED'}")
    
    print("   Force removal attempt...")
    result = library.force_remove_book("1122334455")
    print(f"   Result: {'SUCCESS' if result else 'FAILED'}")
    print(f"   Books remaining: {len(library.books)}")
    
    # Check borrowing history
    history = library.get_borrowing_history("Jane Smith")
    print(f"   Jane Smith's borrowing record was automatically returned: {history[0].return_date is not None}")
    
    print("\n=== Bug Fix Summary ===")
    print("✓ Books cannot be removed while borrowed")
    print("✓ Books can be removed after being returned")
    print("✓ Force removal option available for admin use")
    print("✓ Borrowing records are handled appropriately")


if __name__ == "__main__":
    main()
