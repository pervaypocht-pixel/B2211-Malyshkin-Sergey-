class Threat:
    def __init__(self, description, level, zone):
        self.description = description
        self.level = level
        self.zone = zone

    def info(self):
        print(f"Описание: {self.description}")
        print(f"Уровень опасности: {self.level}")
        print(f"Зона: {self.zone}")

    def escalate(self):
        self.level = min(5, self.level + 1)


class CyberThreat(Threat):
    def __init__(self, description, level, zone, attack_type):
        super().__init__(description, level, zone)
        self.attack_type = attack_type

    def escalate(self):
        self.level = min(5, self.level + 2)


class PhysicalThreat(Threat):
    def __init__(self, description, level, zone, location):
        super().__init__(description, level, zone)
        self.location = location

    def escalate(self):
        self.level = min(5, self.level + 1)


class Scanner:
    def __init__(self):
        self.cyber_keywords = ["хакер", "вирус", "взлом"]
        self.physical_keywords = ["пожар", "атака", "дрон"]
        self.scanned_count = 0

    def analyze(self, text):
        self.scanned_count += 1

        text_lower = text.lower()

        for word in self.cyber_keywords:
            if word in text_lower:
                return CyberThreat(
                    text,
                    4,
                    "Серверная",
                    "Кибератака"
                )

        for word in self.physical_keywords:
            if word in text_lower:
                return PhysicalThreat(
                    text,
                    3,
                    "Главный сектор",
                    "Неизвестно"
                )

        return Threat(
            text,
            2,
            "Неизвестная зона"
        )

    def get_stats(self):
        print(f"Просканировано угроз: {self.scanned_count}")


class ThreatLog:
    def __init__(self):
        self.threats = []

    def add(self, threat):
        self.threats.append(threat)

    def show(self):
        if len(self.threats) == 0:
            print("Список пуст")
            return

        for threat in self.threats:
            threat.info()
            print()

    def strongest(self):
        if len(self.threats) == 0:
            return None

        return max(self.threats, key=lambda x: x.level)


scanner = Scanner()
log = ThreatLog()

while True:
    print("\n1 - Добавить угрозу")
    print("2 - Показать угрозы")
    print("3 - Самая опасная угроза")
    print("4 - Статистика сканера")
    print("5 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        text = input("Введите описание угрозы: ")

        threat = scanner.analyze(text)

        log.add(threat)

        print("Угроза добавлена")

    elif choice == "2":
        log.show()

    elif choice == "3":
        threat = log.strongest()

        if threat:
            threat.info()
        else:
            print("Список пуст")

    elif choice == "4":
        scanner.get_stats()

    elif choice == "5":
        print("Завершение программы...")
        break

    else:
        print("Неверный выбор")