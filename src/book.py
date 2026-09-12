class Book:
    def __init__(self, title, author, year, copies=1):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies  # спрацює сеттер нижче

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Кількість примірників має бути невід'ємним цілим числом")
        self._copies = value

    def info(self):
        return f"{self.title} ({self.year}) — {self.author}, примірників: {self.copies}"

    def to_dict(self):
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "copies": self.copies,
        }

    def __str__(self):
        return self.info()


class EBook(Book):
    """Наслідування: електронна книга — це книга + розмір файлу."""

    def __init__(self, title, author, year, file_size_mb, copies=1):
        super().__init__(title, author, year, copies)
        self.file_size_mb = file_size_mb

    def info(self):  # поліморфізм — перевизначений метод
        base = super().info()
        return f"{base}, файл: {self.file_size_mb} МБ (електронна)"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "EBook"
        data["file_size_mb"] = self.file_size_mb
        return data