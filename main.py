from library import Library
from user import StudentUser, StaffUser
from book import Book

def main():
    lib = Library("City University Library")

    b1 = Book("9780134685991", "Python Crash Course", "Eric Matthes", 2023)
    b2 = Book("9781234567890", "Operating Systems", "A.Silberschatz", 2020)
    b3 = Book("9780987654321", "Data Structures", "Cormen", 2022)
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    u1 = StudentUser("S1001", "Alice")
    u2 = StaffUser("T2001", "Bob")
    lib.register_user(u1)
    lib.register_user(u2)

    lib.borrow_book(u1, b1)
    lib.borrow_book(u2, b2)
    lib.return_book(u1, b1)

    lib.show_all_books()
    lib.show_all_users()

if __name__ == "__main__":
    main()
