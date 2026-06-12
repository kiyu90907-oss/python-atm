import unittest
from decimal import Decimal

from atm import ATMAccount, ATMError, format_money, parse_amount


class ATMTests(unittest.TestCase):
    def test_deposit_increases_balance(self):
        account = ATMAccount(owner="Yuki", balance=Decimal("100.00"))

        account.deposit(Decimal("50"))

        self.assertEqual(account.balance, Decimal("150.00"))

    def test_withdraw_decreases_balance(self):
        account = ATMAccount(owner="Yuki", balance=Decimal("100.00"))

        account.withdraw(Decimal("25.50"))

        self.assertEqual(account.balance, Decimal("74.50"))

    def test_withdraw_rejects_insufficient_balance(self):
        account = ATMAccount(owner="Yuki", balance=Decimal("100.00"))

        with self.assertRaises(ATMError):
            account.withdraw(Decimal("101"))

    def test_parse_amount_rejects_invalid_input(self):
        with self.assertRaises(ATMError):
            parse_amount("abc")

    def test_format_money(self):
        self.assertEqual(format_money(Decimal("1234567.8")), "1,234,567.80")


if __name__ == "__main__":
    unittest.main()
