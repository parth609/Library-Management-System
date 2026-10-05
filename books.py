books = []

def add_book(book):
    books.append(book)
    print("Book added successfully.")

def display_books():
    print("\n===== Available Books =====")

    if not books:
        print("No books available.")
    else:
        for book in books:
            print("-", book)