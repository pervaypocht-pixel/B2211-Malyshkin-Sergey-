"""
ООП = обьектно орьенторованое програмирование.
Парадігма(підход) = Проц. програм , ООП.
Проц. програм. = набір фенкцій | Алгоритмічна декомпозиція.
ООП = Розбиття на сутності | обьектна декомпозиція.

Как ето работает (ООП) = классификация обьектов и присваивание им характеристик и возможномтей.
Сутність = риба
Обьект = Лосось
Класс = шаблон по которому модно определить к какой сущности подходит обьект (поля класса и методы класса)
"""
class Dog:
    def __init__(self, name, age, breed, weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight


dog1 = Dog(name="Robert",age=6,breed="Golden Retriever",weight=30)
dog2 = Dog(name="Edward",age=7,breed="Dachshund",weight=9.5)

print(f"My dogs name is {dog1.name} , its {dog1.age} years old , its a {dog1.breed}, its weights about {dog1.weight} kg")
print(f"His dogs name is {dog2.name} , its {dog2.age} years old , its a {dog2.breed}, its weights about {dog2.weight} kg")
