from Models.api_model import get_questions, get_categories
from Models.supabase_model import save_player
from views.ui import clear, banner, progress_bar, select_difficulty, show_categories, select_category, select_question_count
import random, time, html
import re


def get_player_name():
    while True:
        name = input("Enter your name: ").strip()
        if not re.match(r"^[A-Za-z0-9 ]", name):
            print("Name can only contain letters, numbers, and spaces.")
            continue
        if len(name) == 0 or len(name) > 10:
            print("Name must be between 1 and 10 characters.")
            continue
        return name

def run_quiz():
    clear()
    banner()

    categories = get_categories()
    if not categories:
        print("Could not load categories.")
        input("\nPress ENTER to exit...")
        return

    show_categories(categories)
    category = select_category(categories)
    clear()
    banner()
    difficulty = select_difficulty()

    input("\nPress ENTER to start the quiz...")

    questions = get_questions(amount=10, difficulty=difficulty, category=category)
    if not questions:
        print("No questions found.")
        input("\nPress ENTER to exit...")
        return

    score = 0
    total = len(questions)

    for i, q in enumerate(questions, 1):
        clear()
        banner()
        progress_bar(i, total)
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(x) for x in q["incorrect_answers"]] + [correct]
        random.shuffle(options)

        print(f"Question {i}: {question}")
        for idx, op in enumerate(options, 1):
            print(f"{idx}) {op}")

        choice = input("\nYour answer (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= 4:
            if options[int(choice)-1] == correct:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong. Correct: {correct}\n")
        else:
            print("Invalid choice.\n")
        time.sleep(1)

    print(f"\nFinal Score: {score}/{total}")
    name = input("Enter your name: ").strip()
    save_player(name, score, total, difficulty)
    input("\nPress ENTER to exit...")

def custom_quiz():

    clear()
    banner()

    categories = get_categories()
    show_categories(categories)
    category_id = select_category(categories)
    difficulty = select_difficulty()
    question_count = select_question_count()

    print("\nLoading questions...\n")
    questions = get_questions(amount=question_count, category=category_id, difficulty=difficulty)

    score = 0
    for i, q in enumerate(questions, 1):
        clear()
        banner()
        progress_bar(i, question_count)
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(x) for x in q["incorrect_answers"]] + [correct]
        random.shuffle(options)

        print(f"Question {i}: {question}")
        for idx, op in enumerate(options, 1):
            print(f"{idx}) {op}")

        try:
            choice = int(input("\nYour answer (1-4): "))
        except ValueError:
            choice = 0

        if 1 <= choice <= 4 and options[choice - 1] == correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer: {correct}\n")

        time.sleep(1.2)

    print(f"\nFinal Score: {score}/{len(questions)}")
    name = get_player_name()
    save_player(name, score, len(questions), difficulty)
    input("\nPress ENTER to return to the menu...")
