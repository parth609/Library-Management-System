from books import add_book, display_books
from student import add_student, display_students

def main():
    print("===== Library Management System =====")

    add_book("Python Programming")
    add_book("Data Structures")

    add_student("Parth")

    display_books()
    display_students()

if __name__ == "__main__":
    main()