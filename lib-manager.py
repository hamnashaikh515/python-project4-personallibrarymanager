import json
import os

data_file = 'library.txt'

def load_library():
    """Loads the library from a file, handling errors gracefully."""
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Library file is corrupted. Starting with an empty library.")
            return []
    return []

def save_library(library):
    """Saves the library to a file."""
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Adds a new book to the library."""
    title = input('Enter the title of the book: ').strip()
    author = input('Enter the author of the book: ').strip()
    
    while True:
        try:
            publication_year = int(input('Enter the publication year of the book: '))
            break
        except ValueError:
            print("Invalid input! Please enter a valid year.")

    genre = input('Enter the genre of the book: ').strip()
    read = input('Have you read this book? (yes/no): ').strip().lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f'✅ Book "{title}" added successfully!')

def remove_book(library):
    """Removes a book by title."""
    title = input('Enter the book title to remove: ').strip().lower()
    initial_length = len(library)
    
    library = [book for book in library if book['title'].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f'✅ Book "{title}" removed successfully.')
    else:
        print(f'❌ Book "{title}" not found.')

    return library  # Ensure changes reflect in the main function

def search_library(library):
    """Searches books by title or author."""
    search_by = input('Search by title or author: ').strip().lower()
    if search_by not in ['title', 'author']:
        print("Invalid choice! Please search by 'title' or 'author'.")
        return
    
    search_term = input(f'Enter the {search_by}: ').strip().lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\n📚 Search Results:")
        for book in results:
            status = "Read ✅" if book['read'] else "Unread ❌"
            print(f"- {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")
    else:
        print(f'❌ No books found for "{search_term}" in {search_by}.')

def display_all_books(library):
    """Displays all books sorted by year."""
    if not library:
        print('📖 The library is empty.')
        return

    sorted_library = sorted(library, key=lambda x: x['publication_year'])
    
    print("\n📚 Your Library Collection:")
    for book in sorted_library:
        status = "Read ✅" if book['read'] else "Unread ❌"
        print(f"- {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Displays reading statistics."""
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books else 0

    print("\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"✅ Books read: {read_books} ({percentage_read:.2f}%)")

def main():
    """Main program loop."""
    library = load_library()

    while True:
        print("\n📖 Welcome to Library Manager! 📖")
        print("1️⃣ Add a book")
        print("2️⃣ Remove a book")
        print("3️⃣ Search for a book")
        print("4️⃣ Display all books")
        print("5️⃣ Display statistics")
        print("6️⃣ Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)  # Ensure updated library
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Library saved to file. 👋 Goodbye! ")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
