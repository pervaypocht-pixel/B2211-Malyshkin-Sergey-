import random


class Student:
    def __init__(self, name, age, university, money=100, knowledge=50, energy=100):
        self.name = name
        self.age = age
        self.university = university
        self.money = money
        self.knowledge = knowledge
        self.energy = energy
        self.alive = True

    def study(self):
        print(f"{self.name} учится")
        self.knowledge += 10
        self.energy -= 15
        self.money -= 5

    def work(self):
        print(f"{self.name} работает")
        self.money += 40
        self.energy -= 20
        self.knowledge -= 5

    def rest(self):
        print(f"{self.name} отдыхает")
        self.energy += 25
        self.money -= 20

    def check_status(self):
        print(
            f"День завершён | Деньги: {self.money} | "
            f"Знания: {self.knowledge} | Энергия: {self.energy}"
        )

        if self.money <= 0:
            print(f"{self.name} остался без денег")
            self.alive = False

        elif self.knowledge <= 0:
            print(f"{self.name} был отчислен")
            self.alive = False

        elif self.energy <= 0:
            print(f"{self.name} слишком устал")
            self.alive = False

    def live_one_day(self, day):
        print(f"\n------ День {day} ------")

        if self.money < 30:
            self.work()

        elif self.knowledge < 40:
            self.study()

        elif self.energy < 30:
            self.rest()

        else:
            action = random.choice([self.study, self.work, self.rest])
            action()

        self.check_status()


student1 = Student(
    name="Alex",
    age=21,
    university="Harvard University"
)

for day in range(1, 366):
    if student1.alive:
        student1.live_one_day(day)
    else:
        print(f"\n{student1.name} не смог прожить год")
        break

if student1.alive:
    print(f"\n{student1.name} успешно прожил год")