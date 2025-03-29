"""Игра 'Угадай пропущенное число прогрессии'"""

import random

def generate_progression():
    """Генерирует арифметическую прогрессию с пропущенным элементом"""
    length = 10
    step = random.randint(1, 5)
    start = random.randint(1, 20)
    hidden_idx = random.randint(0, length - 1)
    progression = [start + i * step for i in range(length)]
    answer = progression[hidden_idx]
    progression[hidden_idx] = ".."
    return progression, answer

game_config = {
    'name': 'Угадай число в прогрессии',
    'rounds': 3,
    'generate_round': generate_progression,
    'format_question': lambda data: "Прогрессия: " + " ".join(map(str, data)),
    'prompt': 'Введите пропущенное число: '
}
