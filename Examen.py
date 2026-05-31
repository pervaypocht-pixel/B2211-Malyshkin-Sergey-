class Threat:
    def __init__(self, description, level):
        self.description = description
        self.level = level

    def info(self):
        print(f"Описание: {self.description}")
        print(f"Уровень опасности: {self.level}")

    def escalate(self):
        self.level += 1


class CyberThreat(Threat):
    def escalate(self):
        self.level += 2


class PhysicalThreat(Threat):
    def escalate(self):
        self.level += 1