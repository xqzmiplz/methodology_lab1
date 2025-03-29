"""Главное меню выбора игр"""

from guess_progression import game_config as progression_game
from find_lcm import game_config as lcm_game
from run_game import run_game

def show_menu(games: dict) -> str:
    """Отображает главное меню и возвращает выбор пользователя"""
    print("\nВыберите игру:")
    for key, config in games.items():
        print(f"{key}. {config['name']}")
    print("0. Выход")
    return input("> ").strip()

def main():
    """Основная функция запуска приложения"""
    games = {
        "1": progression_game,
        "2": lcm_game
    }

    while True:
        choice = show_menu(games)
        if choice == "0":
            break
        if choice in games:
            game_config = games[choice]
            run_game(game_config)
        else:
            print("Неверный ввод! Попробуйте снова.")

if __name__ == "__main__":
    main()
