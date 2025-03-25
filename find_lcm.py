"""Игра 'Вычисли НОК трех чисел'"""

import random
from math import gcd
from utils import print_message, read_number

def lcm(a: int, b: int) -> int:
    """Вычисляет НОК для двух чисел"""
    return a * b // gcd(a, b)

def three_numbers_lcm(x: int, y: int, z: int) -> int:
    """Вычисляет НОК для трех чисел"""
    return lcm(lcm(x, y), z)

def play_find_lcm():
    """Запускает игру с 3 раундами"""
    print_message("\n=== Вычисли НОК трех чисел ===")
    correct = 0
    for _ in range(3):
        numbers = [random.randint(2, 50) for _ in range(3)]
        answer = three_numbers_lcm(*numbers)
        print_message(f"Числа: {', '.join(map(str, numbers))}")
        user_answer = read_number("Ваш ответ: ")
        if user_answer == answer:
            correct += 1
            print_message("Верно!")
        else:
            print_message(f"Неверно! Правильный ответ: {answer}")
    print_message(f"\nИгра завершена! Правильных ответов: {correct}/3")
