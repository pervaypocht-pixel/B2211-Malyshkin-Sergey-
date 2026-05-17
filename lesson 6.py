class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Health:", self.health)

    def sound(self):
        print("Animal made a sound")


class WildAnimal(Animal):
    def __init__(self, name, age, danger):
        super().__init__(name, age)
        self.danger = danger

    def attack(self):
        print(self.name, "attacks")


class Predator(WildAnimal):
    def __init__(self, name, age, danger, food_list):
        super().__init__(name, age, danger)
        self.food_list = food_list

    def hunt(self):
        print(self.name, "hunts")
        print("Food list:", self.food_list)


class Lion(Predator):
    def __init__(self, name, age, danger, food_list):
        super().__init__(name, age, danger, food_list)

    def sound(self):
        print(self.name, "roars violently")


class Tiger(Predator):
    def __init__(self, name, age, danger, food_list):
        super().__init__(name, age, danger, food_list)

    def sound(self):
        print(self.name, "roars aggressively")


class Wolf(Predator):
    def __init__(self, name, age, danger, food_list):
        super().__init__(name, age, danger, food_list)

    def sound(self):
        print(self.name, "howls wildly")


class Herbivorous(Animal):
    def __init__(self, name, age, grass_amount):
        super().__init__(name, age)
        self.grass_amount = grass_amount

    def eat_grass(self):
        print(self.name, "eats", self.grass_amount, "kg of grass per day")


class Wildebeest(Herbivorous):
    def __init__(self, name, age, grass_amount):
        super().__init__(name, age, grass_amount)

    def sound(self):
        print(self.name, "snorts loudly")


class Hare(Herbivorous):
    def __init__(self, name, age, grass_amount):
        super().__init__(name, age, grass_amount)

    def sound(self):
        print(self.name, "makes a quiet squeak")


class Deer(Herbivorous):
    def __init__(self, name, age, grass_amount):
        super().__init__(name, age, grass_amount)

    def sound(self):
        print(self.name, "makes a deer call")


lion = Lion("Lion", 12, "violent", ["Deer", "Hare"])
lion.info()
lion.sound()
lion.attack()
lion.hunt()

tiger = Tiger("Tiger", 14, "aggressive", ["Deer", "Wildebeest"])
tiger.info()
tiger.sound()
tiger.attack()
tiger.hunt()

wolf = Wolf("Wolf", 9, "uncontrollable", ["Hare", "Deer"])
wolf.info()
wolf.sound()
wolf.attack()
wolf.hunt()

wildebeest = Wildebeest("Wildebeest", 7, 35)
wildebeest.info()
wildebeest.sound()
wildebeest.eat_grass()

hare = Hare("Hare", 3, 5)
hare.info()
hare.sound()
hare.eat_grass()

deer = Deer("Deer", 6, 12)
deer.info()
deer.sound()
deer.eat_grass()