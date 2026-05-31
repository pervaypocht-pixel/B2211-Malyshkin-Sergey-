
class BankAccount:
    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути більше 0")

        self.money += amount
        print("Поповнено:", amount)
        print("Баланс:", self.money)

    def withdraw(self, amount):
        if amount == 0:
            raise ValueError("Не можна знімати 0 грн")

        if amount < 0:
            raise ValueError("Не можна знімати від'ємну суму")

        if amount > self.money:
            shortage = amount - self.money

            answer = input(
                f"Не вистачає {shortage} грн. Бажаєте взяти кредит? (y/n): "
            )

            if answer.lower() == "y":
                days = int(input("На скільки днів кредит? "))

                if days <= 30:
                    percent = 0.03
                else:
                    percent = 0.04

                repayment = shortage * (1 + percent)

                print(f"Кредит видано: {shortage:.2f} грн")
                print(f"До повернення: {repayment:.2f} грн")
            else:
                print("Операцію скасовано")

            return

        self.money -= amount
        print("Знято:", amount)
        print("Залишок:", self.money)


account = BankAccount(100)

try:
    action = input("Що зробити? (add/withdraw): ")

    if action == "add":
        amount = int(input("Скільки додати? "))
        account.add_money(amount)

    elif action == "withdraw":
        take = int(input("Скільки зняти? "))
        account.withdraw(take)

    else:
        print("Невідома команда")

except ValueError as e:
    print("Помилка:", e)