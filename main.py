import requests
import html
import random
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_questions(amount=10):
    url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple"}
    response = requests.get(url, params=params)
    return response.json()["results"]

def run_quiz():
    clear()
    print("=== OPEN TRIVIA QUIZ ===\n")
    questions = get_questions(10)
    score = 0

    for i, q in enumerate(questions, 1):
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
            print(f"Wrong. Correct: {correct}\n")

        time.sleep(1)

    print(f"Final Score: {score}/{len(questions)}")
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    run_quiz()
