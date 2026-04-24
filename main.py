from services import BankService

def start_bank():
    bank = BankService()
    
    print("Система управления банком.")

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Открыть новый счет")
        print("2. Положить деньги")
        print("3. Снять наличные")
        print("4. Перевести другому клиенту")
        print("5. Посмотреть историю операций")
        print("6. Узнать баланс")
        print("7. Выход")
        
        choice = input("\nВведите номер действия: ").strip()

        if choice == "1":
            acc_id = input("Придумайте ID для счета: ")
            name = input("Введите имя владельца: ")
            print("Выберите тип: 1 - Обычный, 2 - Накопительный")
            acc_type = input("Ваш выбор: ")
            result = bank.create_account(acc_id, name, acc_type)
            print(f"-> {result}")

        elif choice == "2":
            acc_id = input("Введите ID счета: ")
            try:
                amount = float(input("Какую сумму вносим? "))
                print(f"-> {bank.deposit(acc_id, amount)}")
            except ValueError:
                print("! Ошибка: нужно вводить только цифры")

        elif choice == "3":
            acc_id = input("Введите ID счета: ")
            try:
                amount = float(input("Сколько хотите снять? "))
                print(f"-> {bank.withdraw(acc_id, amount)}")
            except ValueError:
                print("! Ошибка: сумма должна быть числом")

        elif choice == "4":
            sender = input("ID вашего счета (откуда): ")
            receiver = input("ID счета получателя (куда): ")
            try:
                amount = float(input("Сумма перевода: "))
                print(f"-> {bank.transfer(sender, receiver, amount)}")
            except ValueError:
                print("! Ошибка: некорректная сумма")

        elif choice == "5":
            acc_id = input("Введите ID для просмотра истории: ")
            acc = bank.accounts.get(acc_id)
            if acc:
                print(f"\n--- История операций по счету {acc_id} ---")
                for i, op in enumerate(acc.history, 1):
                    print(f"{i}. {op}")
            else:
                print("! Указанный счет не найден в базе")

        elif choice == "6":
            acc_id = input("Введите ID счета: ")
            acc = bank.accounts.get(acc_id)
            if acc:
                print(f"На вашем счету сейчас: {acc.balance} руб.")
            else:
                print("! Такого счета не существует")

        elif choice == "7":
            print("Завершаем работу. Хорошего дня!")
            break
        
        else:
            print("Неверный ввод, попробуйте еще раз.")

if __name__ == "__main__":
    try:
        start_bank()
    except KeyboardInterrupt:
        print("\nПрограмма закрыта.")