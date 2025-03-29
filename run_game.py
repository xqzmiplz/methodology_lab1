"""Движок игр"""
from utils import print_message, read_number

def run_game(game_config):
    """Запускает игру с использованием переданной конфигурации"""
    print_message(f"\n=== {game_config['name']} ===")
    correct = 0
    for _ in range(game_config['rounds']):
        question_data, correct_answer = game_config['generate_round']()
        question_text = game_config['format_question'](question_data)
        print_message(question_text)
        user_answer = read_number(game_config['prompt'])
        if user_answer == correct_answer:
            correct += 1
            print_message("Верно!")
        else:
            print_message(f"Неверно! Правильный ответ: {correct_answer}")
    print_message(f"\nИгра завершена! Правильных ответов: {correct}/{game_config['rounds']}")
