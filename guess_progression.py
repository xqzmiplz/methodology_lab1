"""Игра 'Угадай пропущенное число в прогрессии'"""

import random
from utils import print_message, read_number

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

def play_guess_progression():
    """Запускает игру с 3 раундами"""
    print_message("\n=== Угадай число в прогрессии ===")
    correct = 0
    for _ in range(3):
        progression, answer = generate_progression()
        print_message("Прогрессия: " + " ".join(map(str, progression)))
        user_answer = read_number("Введите пропущенное число: ")
        if user_answer == answer:
            correct += 1
            print_message("Верно!")
        else:
            print_message(f"Неверно! Правильный ответ: {answer}")
    print_message(f"\nИгра завершена! Правильных ответов: {correct}/3")
