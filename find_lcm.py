"""Игра 'Вычисли НОК трех чисел'"""

import random
from math import gcd

def lcm(a: int, b: int) -> int:
    """Вычисляет НОК для двух чисел"""
    return a * b // gcd(a, b)

def three_numbers_lcm(x: int, y: int, z: int) -> int:
    """Вычисляет НОК для трех чисел"""
    return lcm(lcm(x, y), z)

def generate_lcm_round():
    """"Генерирует случайные числа"""
    numbers = [random.randint(2, 50) for _ in range(3)]
    answer = three_numbers_lcm(*numbers)
    return numbers, answer

game_config = {
    'name': 'Вычисли НОК трех чисел',
    'rounds': 3,
    'generate_round': generate_lcm_round,
    'format_question': lambda data: f"Числа: {', '.join(map(str, data))}",
    'prompt': 'Ваш ответ: '
}
