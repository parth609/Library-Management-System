books = []

def add_book(book):
    books.append(book)
    print("Book added successfully.")

def remove_book(book):
    if book in books:
        books.remove(book)
        print("Book removed successfully.")

def display_books():
    print("Available Books:")
    for book in books:
        print(book)