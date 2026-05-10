class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Character:
    def __init__(self, name, lvl, weapon, armor):
        self.name = name
        self.lvl = lvl
        self.weapon = weapon
        self.armor = armor

    def ch_info(self):
        print(f"{self.name}, lvl {self.lvl}")
        print(f"Weapon: {self.weapon.name} (damage = {self.weapon.damage})")

    def ch_attack(self, enemy1):
        print(f"{enemy1.name} approaching! (health = {enemy1.health})")
        print(f"{enemy1.name} got hit by {self.name}'s {self.weapon.name}")

        enemy1.health -= self.weapon.damage

        print(f"{enemy1.name} remaining hp is {enemy1.health}!")


weapon1 = Weapon(name="French miniBow", damage=6)
weapon2 = Weapon(name="Baguette Magic Wand", damage=7)

enemy1 = Enemy(name="French Zombie", health=999999999)

armor1 = Armor(name="Swagowaja koftochka i shtanishki" , defense=1)
armor2 = Armor(name="Spanish Burrito Armor", defense=9999)

character1 = Character(name="Francua", lvl=24, weapon=weapon1, armor=armor1)
character1.ch_info()
character1.ch_attack(enemy1)

character2 = Character(name="El Mochacho", lvl=36, weapon=weapon2, armor=armor2)
character2.ch_info()
character2.ch_attack(enemy1)