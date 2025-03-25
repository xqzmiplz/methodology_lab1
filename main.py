"""Главное меню выбора игр"""

from guess_progression import play_guess_progression
from find_lcm import play_find_lcm

def show_menu() -> str:
    """Отображает главное меню и возвращает выбор пользователя"""
    print("\nВыберите игру:")
    print("1. Угадай число в прогрессии")
    print("2. Вычисли НОК трех чисел")
    print("0. Выход")
    return input("> ").strip()

def main():
    """Основная функция запуска приложения"""
    games = {
        "1": ("Угадай число в прогрессии", play_guess_progression),
        "2": ("Вычисли НОК трех чисел", play_find_lcm)
    }

    while True:
        choice = show_menu()
        if choice == "0":
            break
        if choice in games:
            games[choice][1]()
        else:
            print("Неверный ввод! Попробуйте снова.")

if __name__ == "__main__":
    main()
