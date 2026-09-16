from book import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]

    def find_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def total_books(self):
        return sum(b.copies for b in self.books)

    def show_all(self):
        for b in self.books:
            print(b)