class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        self.inventory = []

    def info(self):
        print(f"\n=== {self.name} ===")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")

    def attack(self):
        print(f"{self.name} attacks with a basic hit!")

    def rest(self):
        self.health += 10
        print(f"{self.name} takes a nap in the bushes and restores 10 HP.")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} was added to {self.name}'s inventory.")

    def show_inventory(self):
        print(f"{self.name}'s inventory: {self.inventory}")


class Warrior(Character):
    def __init__(self, name, level, health, strength, energy):
        super().__init__(name, level, health)
        self.strength = strength
        self.energy = energy

    def attack(self):
        print(f"{self.name} smashes the enemy with a giant sword!")

    def strong_attack(self):
        if self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} uses Strong Attack!")
            print(f"Energy left: {self.energy}")
        else:
            print(f"{self.name} does not have enough energy!")

    def shield_block(self):
        print(f"{self.name} blocks the attack with a frying pan shield!")


class Mage(Character):
    def __init__(self, name, level, health, tacoenergy, magic_power):
        super().__init__(name, level, health)
        self.tacoenergy = tacoenergy
        self.magic_power = magic_power

    def attack(self):
        print(f"{self.name} throws a giant flaming meatball!")

    def cast_spell(self):
        if self.tacoenergy >= 30:
            self.tacoenergy -= 30
            print(f"{self.name} casts a chaotic spaghetti spell!")
            print(f"TacoEnergy left: {self.tacoenergy}")
        else:
            print(f"{self.name} does not have enough TacoEnergy!")

    def teleport(self):
        if self.tacoenergy >= 15:
            self.tacoenergy -= 15
            print(f"{self.name} teleports directly to the fridge!")
            print(f"TacoEnergy left: {self.tacoenergy}")
        else:
            print(f"{self.name} does not have enough TacoEnergy!")


class Archer(Character):
    def __init__(self, name, level, health, arrows, agility):
        super().__init__(name, level, health)
        self.arrows = arrows
        self.agility = agility

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self.name} shoots an exploding cucumber arrow!")
            print(f"Arrows left: {self.arrows}")
        else:
            print(f"{self.name} has no arrows left!")

    def dodge(self):
        print(f"{self.name} performs a ninja refrigerator dodge!")

    def rapid_shot(self):
        if self.arrows >= 3:
            self.arrows -= 3
            print(f"{self.name} uses Rapid Shot!")
            print(f"Arrows left: {self.arrows}")
        else:
            print(f"{self.name} does not have enough arrows!")


class BossMage(Mage):
    def __init__(self, name, level, health, tacoenergy, magic_power, boss_skill):
        super().__init__(name, level, health, tacoenergy, magic_power)
        self.boss_skill = boss_skill

    def ultimate_spell(self):
        if self.tacoenergy >= 50:
            self.tacoenergy -= 50
            print(f"{self.name} uses ULTIMATE SPELL: {self.boss_skill}!")
            print(f"TacoEnergy left: {self.tacoenergy}")
        else:
            print(f"{self.name} does not have enough TacoEnergy for the ultimate spell!")


warrior = Warrior(
    "Sir Dumpling The Destroyer",
    10,
    120,
    50,
    100)

mage = Mage(
    "Lord of the Spaghetti Apocalypse",
    12,
    80,
    120,
    90)

archer = Archer(
    "Count Cucumber Fastlegs",
    11,
    90,
    15,
    95)

boss = BossMage(
    "Dark Shawarma Wizard",
    20,
    200,
    200,
    150,
    "Taco Devourer")

warrior.add_item("French Baguette of Justice")
warrior.add_item("Shield of the Fried Penguin")

mage.add_item("Staff of the Drunken Unicorn")
mage.add_item("Potion of Fizzy Chaos")

archer.add_item("Bow of the Sour Watermelon")
archer.add_item("Quiver of Destiny and Mayonnaise")

heroes = [warrior, mage, archer, boss]

for hero in heroes:
    hero.info()
    hero.attack()
    hero.rest()
    hero.show_inventory()

print("\n=== SPECIAL ABILITIES ===")

warrior.strong_attack()
warrior.shield_block()

mage.cast_spell()
mage.teleport()

archer.rapid_shot()
archer.dodge()

boss.ultimate_spell()