class Book:

    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        print(f"{self.title} by {self.author} status: {self.is_borrowed}")

    def return_book(self):
        self.is_borrowed = False
        print(f"{self.title} can now be returned.")

one = Book("The Sorcerers Stone", "J.K. Rowling", "True")
two = Book("Chamber of secrets", "J.K Rowling", "False")

two.return_book()
