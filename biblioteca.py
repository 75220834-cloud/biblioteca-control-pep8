class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Disponible" if book.available else "Prestado"
            print(
                f"Título: {book.title}, "
                f"Autor: {book.author}, "
                f"Índice: {book.index}, "
                f"Estado: {status}"
            )


class Book:
    def __init__(self, title, author, index):
        self.title = title
        self.author = author
        self.index = index
        self.available = True

    def lend(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True
