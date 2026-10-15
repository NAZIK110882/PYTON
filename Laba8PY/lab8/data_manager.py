"""Робота з користувачами в JSON (перенесено з ЛР 2)."""
import json


def load_users(path):
    """Зчитує список користувачів з JSON-файлу."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON має містити список користувачів")
    return data


def get_users_older_than(users, age):
    """Повертає користувачів, старших за вказаний вік."""
    return [u for u in users if u.get("age", 0) > age]


def load_users_older_than(path, age):
    """Зчитує файл і повертає користувачів, старших за age."""
    return get_users_older_than(load_users(path), age)


def save_users(path, users):
    """Зберігає список користувачів у JSON-файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
