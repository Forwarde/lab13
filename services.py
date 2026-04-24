from models import Account, SavingsAccount

class BankService:
    def __init__(self):
        # Храним все счета в обычном словаре
        self.all_accounts = {}

    def create_account(self, id, name, type):
        if id in self.all_accounts:
            return "Ошибка! Такой ID уже занят, выберите другой."
        
        # Проверяем, какой счет хочет создать юзер
        if type == "2":
            new_acc = SavingsAccount(id, name)
        else:
            new_acc = Account(id, name)
            
        self.all_accounts[id] = new_acc
        return f"Готово! Счет для {name} создан."

    def deposit(self, id, money):
        if id not in self.all_accounts:
            return "Мы не нашли счет с таким ID."
            
        if money <= 0:
            return "Сумма пополнения должна быть плюсовой."
        
        # Обновляем баланс и пишем в историю
        target = self.all_accounts[id]
        target.balance += money
        target.add_history(f"Положил на счет: {money}")
        return "Счет успешно пополнен."

    def withdraw(self, id, money):
        account = self.all_accounts.get(id)
        
        if account is None:
            return "Счет не найден."
            
        if money > account.balance:
            return "На балансе маловато денег для такой суммы."
        
        account.balance -= money
        account.add_history(f"Снял наличные: {money}")
        return f"Вы сняли {money}. Заберите деньги."

    def transfer(self, id_from, id_to, amount):
        # Проверяем наличие обоих счетов
        if id_from not in self.all_accounts or id_to not in self.all_accounts:
            return "Ошибка: проверьте ID отправителя или получателя."
        
        sender = self.all_accounts[id_from]
        receiver = self.all_accounts[id_to]

        if amount > sender.balance:
            return "На вашем счету недостаточно средств для перевода."

        # Сама операция перевода
        sender.balance -= amount
        receiver.balance += amount
        
        # Записываем историю обоим участникам
        sender.add_history(f"Перевел {amount} пользователю {id_to}")
        receiver.add_history(f"Получил перевод {amount} от {id_from}")
        
        return "Деньги успешно переведены."