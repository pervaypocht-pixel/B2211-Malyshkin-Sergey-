class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, player):
        print(f"{self.name} атакует {player.name}!")
        player.hp -= self.damage
        print(f"{player.name} потерял {self.damage} хп!")
        print(f"Осталось хп у {player.name}: {player.hp}\n")


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []

    def player_info(self):
        print(f"Игрок: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Урон: {self.damage}\n")

    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}!")
        enemy.hp -= self.damage
        print(f"{enemy.name} потерял {self.damage} хп!")
        print(f"Осталось хп у {enemy.name}: {enemy.hp}\n")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} добавлен в инвентарь!\n")

    def show_inventory(self):
        print(f"Инвентарь {self.name}:")

        if len(self.inventory) == 0:
            print("Инвентарь пуст.\n")
        else:
            for item in self.inventory:
                print(f"- {item.name} (ценность = {item.value})")
            print()


item1 = Item(name="Картошка Фри Судьбы", value=50)
item2 = Item(name="Тако Бесконечности", value=100)

player1 = Player(name="Добрый Огурец", hp=100, damage=20)

enemy1 = Enemy(name="Злой Огурец", hp=80, damage=15)

player1.player_info()

player1.add_item(item1)
player1.add_item(item2)

player1.show_inventory()

print("=== БОЙ НАЧАЛСЯ ===\n")

while player1.hp > 0 and enemy1.hp > 0:

    player1.attack(enemy1)

    if enemy1.hp <= 0:
        print(f"{enemy1.name} уничтожен!")
        break

    enemy1.attack(player1)

    if player1.hp <= 0:
        print(f"{player1.name} проиграл!")
        break

print("\n=== БОЙ ЗАКОНЧЕН ===")
