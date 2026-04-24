import unittest
from services import BankService

class TestBank(unittest.TestCase):
    def setUp(self):
        self.service = BankService()
        self.service.create_account("1", "Ivan")
        self.service.create_account("2", "Alice")

    # 1 Проверка пополнения
    def test_deposit(self):
        self.service.deposit("1", 500)
        # Проверяем, что на балансе ровно 500
        self.assertEqual(self.service.accounts["1"].balance, 500)

    # 2 Проверка снятия (ошибка при нехватке средств)
    def test_withdraw_insufficient(self):
        res = self.service.withdraw("1", 1000)
        self.assertEqual(res, "Недостаточно средств!")
        
    def test_transfer(self):
        self.service.deposit("1", 300)
        self.service.transfer("1", "2", 100)
        # У Ивана должно остаться 200, у Алисы стать 100
        self.assertEqual(self.service.accounts["2"].balance, 100)

if __name__ == "__main__":
    unittest.main()