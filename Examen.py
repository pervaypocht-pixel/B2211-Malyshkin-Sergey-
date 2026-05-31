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


class Scanner:
    def analyze(self, text):

        text = text.lower()

        if "хакер" in text or "вирус" in text or "взлом" in text:
            return CyberThreat(text, 4)

        if "пожар" in text or "атака" in text or "дрон" in text:
            return PhysicalThreat(text, 3)

        return Threat(text, 2)