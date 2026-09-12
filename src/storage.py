import json
from book import Book, EBook


class JSONStorage:
    @staticmethod
    def save(library, filename):
        data = [b.to_dict() for b in library.books]
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"Помилка запису файлу: {e}")

    @staticmethod
    def load(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Файл не знайдено, повертаю порожній список.")
            return []
        except json.JSONDecodeError:
            print("Файл пошкоджено або має неправильний формат.")
            return []

        books = []
        for item in data:
            if item.get("type") == "EBook":
                books.append(EBook(item["title"], item["author"], item["year"],
                                    item["file_size_mb"], item["copies"]))
            else:
                books.append(Book(item["title"], item["author"], item["year"], item["copies"]))
        return books