import os, sys, time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("╔" + "═" * 38 + "╗")
    print("║{:^38}║".format("OPEN TRIVIA QUIZ APP"))
    print("╚" + "═" * 38 + "╝")

def progress_bar(current, total, length=20):
    filled = int(length * current // total)
    bar = "█" * filled + "-" * (length - filled)
    print(f"[{bar}] {current}/{total}")

def show_categories(categories):
    print("\nAvailable Categories:\n")
    for c in categories:
        print(f"{c['id']:>3}) {c['name']}")


#! Si las miradas mataran]
#! La tuya me hizo el amor
#! Se ve que tú estás a vapor
#! Ella mata con traje y cuando se viste sport
#! Tiene el booty XL, pero usa los panties small


def select_category(categories):
    try:
        cat_id = int(input("\nEnter category ID: "))
        if any(c['id'] == cat_id for c in categories):
            return cat_id
    except ValueError:
        pass
    print("Invalid selection, defaulting to General Knowledge.")
    return 9

def select_difficulty():
    print("\nSelect difficulty:")
    print("1) easy\n2) medium\n3) hard")
    choice = input("> ").strip()
    return {"1": "easy", "2": "medium", "3": "hard"}.get(choice, "easy")

def select_question_count():
    try:
        count = int(input("\nHow many questions? (1-50): "))
        return max(1, min(count, 50))
    except ValueError:
        return 10
