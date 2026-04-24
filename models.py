# Базовый класс для всех счетов
class Account:
    def __init__(self, id, owner_name, start_balance=0):
        self.id = id
        self.owner = owner_name
        self.balance = start_balance
        self.history = [] # Тут будем хранить записи об операциях

    def add_history(self, action_text):
        # Просто добавляем строку в список
        self.history.append(action_text)

    def __str__(self):
        return f"ID: {self.id}, Владелец: {self.owner}, На счету: {self.balance}"

# Дочерний класс для накопительного счета
class SavingsAccount(Account):
    def __init__(self, id, owner_name, start_balance=0, rate=0.05):
        # Вызываем конструктор родителя
        super().__init__(id, owner_name, start_balance)
        self.rate = rate

    def __str__(self):
        # Берем строку из родительского класса и добавляем инфу про процент
        base_info = super().__str__()
        return f"{base_info} (Процентная ставка: {self.rate * 100}%)"