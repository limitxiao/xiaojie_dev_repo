#!/usr/bin/env python3
"""
Example usage of the Library Management System.
This script demonstrates the basic functionality and contains the bugs/missing features.
"""

from library.manager import LibraryManager
from datetime import datetime, timedelta


def main():
    """Main demonstration function."""
    print("=== Library Management System Demo ===\n")
    
    # Create a library manager
    library = LibraryManager()
    
    # Add some books
    print("Adding books to the library...")
    library.add_book("1984", "George Orwell", "1234567890", 1949)
    library.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321", 1960)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455", 1925)
    library.add_book("Animal Farm", "George Orwell", "5566778899", 1945)
    
    # Demonstrate the bug: Search is case-sensitive for ISBN
    print("\nSearching for books...")
    results = library.search_books("1984")
    print(f"Search for '1984': {len(results)} result(s)")
    
    # This will demonstrate the search bug
    results = library.search_books("1234567890")  # ISBN search
    print(f"Search for ISBN '1234567890': {len(results)} result(s)")
    
    # Borrow some books
    print("\nBorrowing books...")
    library.borrow_book("1234567890", "Alice Johnson")
    library.borrow_book("0987654321", "Bob Smith")
    
    # Demonstrate the bug: Can remove borrowed books
    print("\nAttempting to remove a borrowed book (this should fail but doesn't)...")
    removed = library.remove_book("1234567890")  # This book is borrowed!
    print(f"Removed borrowed book: {removed}")
    
    # Show current status
    print(f"\nLibrary Report:")
    report = library.generate_report()
    for key, value in report.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    # Show available books
    print(f"\nAvailable books:")
    available = library.get_available_books()
    for book in available:
        print(f"  - {book.title} by {book.author}")
    
    # Demonstrate missing features
    print(f"\nMissing Features Demonstrated:")
    print(f"  - No genre classification for books")
    print(f"  - No rating system")
    print(f"  - No popular books statistics in reports")
    print(f"  - No revenue calculation from fines")
    print(f"  - Fine calculation doesn't account for weekends/holidays")
    print(f"  - ISBN validation is incomplete (only checks length)")


if __name__ == "__main__":
    main()
