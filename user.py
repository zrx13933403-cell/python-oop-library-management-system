class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_limit(self):
        return 0

    def __str__(self):
        return f"{self.user_id} - {self.name}"

class StudentUser(User):
    def borrow_limit(self):
        return 5

class StaffUser(User):
    def borrow_limit(self):
        return 10
