import random
import time

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Выполнение атаки на другого героя."""
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        """Проверка, жив ли герой."""
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name='Компьютер'):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Начало игры и чередование ходов."""
        turn = 0  # Счетчик ходов, четные ходы - игрок, нечетные - компьютер
        while self.player.is_alive() and self.computer.is_alive():
            print("\nТекущее состояние героев:")
            print(f"{self.player.name} - Здоровье: {self.player.health}")
            print(f"{self.computer.name} - Здоровье: {self.computer.health}")
            time.sleep(1)  # Пауза для лучшей читаемости

            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            turn += 1

        # Определение победителя
        if self.player.is_alive():
            print(f"\nПобедил {self.player.name}!")
        else:
            print(f"\nПобедил {self.computer.name}!")

# Основная часть программы
if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()
