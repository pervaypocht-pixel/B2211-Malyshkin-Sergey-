class Character:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.health = 100
    def ch_info(self):
        print(f"{self.name} , lvl - {self.lvl} , health - {self.health}")

class Mage(Character):
    def __init__(self, name, lvl, fp):
        super().__init__(name, lvl)
        self.fp = fp


class Samurai(Character):
    def __init__(self, name, lvl, spirit):
        super().__init__(name, lvl)
        self.spirit = spirit