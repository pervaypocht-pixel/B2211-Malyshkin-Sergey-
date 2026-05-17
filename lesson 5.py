class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        self.health = 100

    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Health:",self.health)

    def sound(self):
        print("Animal made a sound")

class WildAnimal(Animal):
    def __init__(self,name,age,danger):
        super().__init__(name,age)
        self.danger = danger
    def attack(self):
        print(self.name,"attacks")

class Lion(WildAnimal):
    def __init__(self,name,age,danger):
        super().__init__(name,age,danger)
        self.roar_power = 100

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    def sound(self):
        print("Dog barks")

    def info(self):
        super().info()
        print("breeed:",self.breed)

class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def sound(self):
        print("Cat meows")

    def info(self):
        super().info()
        print("color:",self.color)

class Bird(Animal):
    def __init__(self,name,age,wings_length):
        super().__init__(name,age)
        self.wings_length = wings_length

    def sound(self):
        print("Bird meows")

    def info(self):
        super().info()
        print("wings length:",self.wings_length)


dog = Dog(name="MangoEater1337",age=4,breed="duschhund")
dog.info()
dog.sound()
cat = Cat(name="MangoAbominator",age=6,color="orange")
cat.info()
cat.sound()
bird = Bird(name="Robert",age=7,wings_length=53)
bird.info()
bird.sound()