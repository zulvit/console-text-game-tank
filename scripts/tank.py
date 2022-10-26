import random


class Tank:
    model: str
    armor: int
    damage: int
    health: int

    def __init__(self, model: str, armor: int, min_damage: int, max_damage: int, health: int):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def print_info(self):
        print(
            f"{self.model} имеет лобовую броню {self.armor} мм. "
            f"при {self.health} ед. здоровья и урон в {self.damage} единиц"
        )

    def shot(self, enemy):
        enemy.health_down(self.damage)
        if enemy.health <= 0:
            print(f"Экипаж танка {enemy.model} уничтожен")
        else:
            print(f"{self.model}: Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")

    def health_down(self, damage: int):
        self.health -= int(damage / self.armor)
        print(
            f"{self.model}: коммандир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья"
        )


if __name__ == "__main__":
    cmd = input("Введите команду ")

    while cmd != "stop":
        tank_1 = Tank(
            input("Введите модель танка "),
            int(input("Введите броню танка ")),
            int(input("Введите минимальный урон ")),
            int(input("Введите максимальный урон ")),
            int(input("Введите здоровье танка "))
        )

        tank_2 = Tank(
            input("Введите модель танка "),
            int(input("Введите броню танка ")),
            int(input("Введите минимальный урон ")),
            int(input("Введите максимальный урон ")),
            int(input("Введите здоровье танка "))
        )
        tank_1.shot(tank_2)
