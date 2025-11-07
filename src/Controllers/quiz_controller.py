import random, time, html
from models.api_model import get_questions
from views.ui import clear, banner, progress_bar, select_difficulty

def run_quiz():
    clear()
    banner()

    difficulty = select_difficulty()
    input("\nPress ENTER to start the quiz...")

    questions = get_questions(amount=10, difficulty=difficulty)
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
                print(" Correct!\n")
                score += 1
            else:
                print(f" Wrong. Correct: {correct}\n")
        else:
            print(" Invalid choice.\n")
        time.sleep(1)

    print(f" Final Score: {score}/{total}")
    input("\nPress ENTER to exit...")

