"""Модуль с общими утилитами для игр"""

def print_message(message: str) -> None:
    """Выводит сообщение в консоль"""
    print(message)

def read_number(prompt: str) -> int:
    """Считывает целое число с проверкой формата"""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print_message("Ошибка: введите целое число!")
