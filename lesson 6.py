class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100

    def info(self):
        print(f"\n--- Информация о животном ---")
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Здоровье: {self.health}")

    def sound(self):
        print(f"{self.name} издает звук")


# ==================== ДИКИЕ ЖИВОТНЫЕ ====================

class WildAnimal(Animal):
    def __init__(self, name, age, danger):
        super().__init__(name, age)
        self.danger = danger

    def attack(self):
        print(f"{self.name} атакует!")
        print(f"Уровень опасности: {self.danger}")


# ==================== ХИЩНИКИ ====================

class Predator(WildAnimal):
    def __init__(self, name, age, danger, food_list):
        super().__init__(name, age, danger)
        self.food_list = food_list

    def hunt(self):
        foods = ", ".join(self.food_list)

        print(f"{self.name} выходит на охоту")
        print(f"Список добычи: {foods}")


class Lion(Predator):
    def sound(self):
        print(f"{self.name} яростно рычит!")


class Tiger(Predator):
    def sound(self):
        print(f"{self.name} агрессивно рычит!")


class Wolf(Predator):
    def sound(self):
        print(f"{self.name} дико воет!")


# ==================== ТРАВОЯДНЫЕ ====================

class Herbivorous(Animal):
    def __init__(self, name, age, grass_amount):
        super().__init__(name, age)
        self.grass_amount = grass_amount

    def eat_grass(self):
        print(f"{self.name} съедает {self.grass_amount} кг травы в день")


class Wildebeest(Herbivorous):
    def sound(self):
        print(f"{self.name} громко фыркает!")


class Hare(Herbivorous):
    def sound(self):
        print(f"{self.name} тихо пищит!")


class Deer(Herbivorous):
    def sound(self):
        print(f"{self.name} издает олений зов!")


# ======================================================
#                    ХИЩНИКИ
# ======================================================

print("\n==============================")
print("      РАЗДЕЛ ХИЩНИКОВ")
print("==============================")

lion = Lion("Лев", 12, "Очень опасный", ["Олень", "Заяц"])

lion.info()
print()
lion.sound()
print()
lion.attack()
print()
lion.hunt()

print("\n--------------------------------")

tiger = Tiger("Тигр", 14, "Агрессивный", ["Олень", "Гну"])

tiger.info()
print()
tiger.sound()
print()
tiger.attack()
print()
tiger.hunt()

print("\n--------------------------------")

wolf = Wolf("Волк", 9, "Непредсказуемый", ["Заяц", "Олень"])

wolf.info()
print()
wolf.sound()
print()
wolf.attack()
print()
wolf.hunt()


# ======================================================
#                  ТРАВОЯДНЫЕ
# ======================================================

print("\n\n==============================")
print("    РАЗДЕЛ ТРАВОЯДНЫХ")
print("==============================")

wildebeest = Wildebeest("Гну", 7, 35)

wildebeest.info()
print()
wildebeest.sound()
print()
wildebeest.eat_grass()

print("\n--------------------------------")

hare = Hare("Заяц", 3, 5)

hare.info()
print()
hare.sound()
print()
hare.eat_grass()

print("\n--------------------------------")

deer = Deer("Олень", 6, 12)

deer.info()
print()
deer.sound()
print()
deer.eat_grass()