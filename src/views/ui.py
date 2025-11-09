import os, sys, time
from views.ui import clear

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
    for i, c in enumerate(categories, start=1):
        print(f"{i:>3}) {c['name']}")

def select_category(categories):
    while True:
        try:
            cat_num = int(input("\nEnter category number: "))
            if 1 <= cat_num <= len(categories):
                return categories[cat_num - 1]['id']
            else:
                clear()
                print("Invalid category number. Please try again.")
                input("Press ENTER to continue...")
        except ValueError:
            print("Please enter a valid number.")
            input("Press ENTER to continue...")
    

def select_difficulty():
    while True:
        print ("\nSelect Difficulty:")
        print("1) Easy\n2) Medium\n3) Hard")
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def select_question_count():
    while True:
        try:
            count = int(input("\nNumber of questions (1-50): "))
            if 1 <= count <= 50:
                return count
            else:
                print("Please choose a number between 1 and 50.")

        except ValueError:  
            print("Invalid input. Please enter a number.")

