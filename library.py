class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book):
        if book in self.books and not book.is_borrowed:
            if len(user.borrowed_books) < user.borrow_limit():
                book.borrow()
                user.borrowed_books.append(book)
                print(f"Borrowed: {book.title}")
                return True
        print("Failed to borrow")
        return False

    def return_book(self, user, book):
        if book in user.borrowed_books:
            book.return_book()
            user.borrowed_books.remove(book)
            print(f"Returned: {book.title}")
            return True
        print("Failed to return")
        return False

    def show_all_books(self):
        print("\n=== Book List ===")
        for b in self.books:
            print(b)

    def show_all_users(self):
        print("\n=== User List ===")
        for u in self.users:
            print(u, "| Limit:", u.borrow_limit())
