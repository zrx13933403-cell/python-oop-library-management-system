class Book:
    def __init__(self, isbn, title, author, year):
        self.__isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def get_isbn(self):
        return self.__isbn

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.__isbn}] {self.title} | {self.author} ({year}) | {status}"
