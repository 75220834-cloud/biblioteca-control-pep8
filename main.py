from biblioteca import Library, Book

library = Library("Central")

book1 = Book("Python", "Guido van Rossum", 1)
book2 = Book("Java", "James Gosling", 2)

library.add_book(book1)
library.add_book(book2)

library.show_books()

print(book1.lend())
print(book1.lend())
book1.return_book()
print(book1.lend())
