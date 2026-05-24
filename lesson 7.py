class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 50
        self.lvl = 1

    def attack(self):
        print(f"{self.name} attacked!")
        self.mana -= 10

    def heal(self):
        print(f"{self.name} healed!")
        self.mana += 10
        self.hp += 10

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 100
        self.lvl = 1

    def superheal(self):
        print(f"{self.name} healed!")
        self.mana -= 20
        self.hp += 20

class Archer(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 35
        self.lvl = 2

    def shoot(self):
        print(f"{self.name} shooted an arrow!")
        self.mana -= 5

hero = Hero("El Mango")
mage = Mage("El Mangolo")
archer = Archer("El Mangolesto")

print(isinstance(hero, Hero))
delattr(hero, "mana")
hp = getattr(hero, "hp")
print(hp)
inv = setattr(hero, "inventory", [])
hero.inventory.append("Mango")
hero.inventory.append("De Mango")
hero.inventory.append("La Mango")
print(hero.inventory)
if hasattr(hero, "inventory"):
    print("hero has an inventory")
print(hero.__dict__)
print(isinstance(mage, Mage))
mana = getattr(mage, "mana")
print(mana)
if hasattr(mage, "inventory"):
    print("mage has an inventory")
print(isinstance(archer, Archer))
lvl = getattr(archer, "lvl")
print(lvl)
setattr(archer, "lvl", 7)
if lvl >= 5:
    setattr(archer, "mana", 70)
    print(lvl)
    print(archer.mana)