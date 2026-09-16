from book import Book, EBook
from library import Library
from storage import JSONStorage

# Створення бібліотеки та книг
library = Library("Міська бібліотека")
library.add_book(Book("Кобзар", "Тарас Шевченко", 1840, 5))
library.add_book(EBook("Дюна", "Френк Герберт", 1965, 12.5, 3))

print("=== Усі книги ===")
library.show_all()

print(f"\nЗагальна кількість примірників: {library.total_books()}")

# Збереження у JSON
JSONStorage.save(library, "library_data.json")
print("\nДані збережено у library_data.json")

# Зчитування назад
loaded_books = JSONStorage.load("library_data.json")
print("\n=== Завантажено з файлу ===")
for b in loaded_books:
    print(b)

# Перевірка захисту від некоректного вводу
try:
    bad_book = Book("Тест", "Автор", 2020, -3)
except ValueError as e:
    print(f"\nПеревірка захисту: {e}")