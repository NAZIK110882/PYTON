"""Клас банківського рахунку (Лабораторна 8, середній рівень)."""


class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self._balance = initial_balance

    def deposit(self, amount):
        """Додає кошти. Сума має бути додатною."""
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self._balance += amount

    def withdraw(self, amount):
        """Знімає кошти. Не можна знімати більше, ніж є на балансі."""
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною")
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self._balance -= amount

    def get_balance(self):
        """Повертає поточний баланс."""
        return self._balance
