"""Математичні утиліти (Лабораторна 8, базовий рівень)."""


def add(a, b):
    """Повертає суму двох чисел."""
    return a + b


def divide(a, b):
    """Ділить a на b. При b == 0 піднімає ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе")
    return a / b


def is_even(n):
    """Перевіряє, чи є ціле число парним."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n має бути цілим числом")
    return n % 2 == 0


def factorial(n):
    """Обчислює факторіал невід'ємного цілого числа."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n має бути цілим числом")
    if n < 0:
        raise ValueError("Факторіал від'ємного числа не визначений")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
