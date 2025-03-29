"""Модуль утилит для взаимодействия с пользователем"""

def print_message(message: str) -> None:
    """Выводит сообщение с дополнительным форматированием"""
    print(f"{message}")


def read_number(prompt: str) -> int:
    """Считывает целое число с обработкой ошибок ввода"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print_message("Ошибка: введите целое число!")
