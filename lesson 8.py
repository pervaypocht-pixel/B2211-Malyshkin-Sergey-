"""try:
    x = int(input())
    result = 10 / x2
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You can't divide by a letter!")
else:
    print(result)
finally:
    print("end")"""
"""try:
    age = int(input())
    if age < 0:
        raise ValueError("Age can't be less than 0!")
    if age == 0:
        raise ValueError("Age can't be 0!")
    print("ok")

except ValueError as e:
    print("error:" , e)
except ValueError as i:
    print("error:" , i)"""

class BankAccount:
    def __init__(self, money):
        self.money = money

    # 2. метод пополнения счета
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
            raise ValueError("Не можна знімати мінус")

        if amount > self.money:
            raise ValueError("Недостатньо грошей")

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