"""Тести для BankAccount (unittest, setUp/tearDown)."""
import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def tearDown(self):
        del self.account

    # --- початковий стан ---
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_default_balance_is_zero(self):
        self.assertEqual(BankAccount().get_balance(), 0)

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            BankAccount(-5)

    # --- deposit ---
    def test_deposit_positive(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # --- withdraw ---
    def test_withdraw_positive(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_all(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(101)
        self.assertEqual(self.account.get_balance(), 100)  # баланс не змінився

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)

    def test_withdraw_zero(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_sequence_of_operations(self):
        self.account.deposit(50)
        self.account.withdraw(120)
        self.assertEqual(self.account.get_balance(), 30)


if __name__ == "__main__":
    unittest.main()
