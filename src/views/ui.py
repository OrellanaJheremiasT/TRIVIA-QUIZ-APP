import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("╔" + "═" * 38 + "╗")
    print("║{:^38}║".format("OPEN TRIVIA QUIZ APP"))
    print("╚" + "═" * 38 + "╝\n")

def progress_bar(current, total):
    length = 20
    completed = int((current / total) * length)
    bar = "#" * completed + "-" * (length - completed)
    print(f"[{bar}] {current}/{total}")

def select_difficulty():
    print("Select difficulty level:")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")

    while True:
        choice = input("Choose (1-3): ")
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def select_category(categories):
    while True:
        try:
            choice = int(input("\nEnter category ID: "))
            if any(cat["id"] == choice for cat in categories):
                return choice
            else:
                print("Invalid category ID. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def show_categories(categories):
 
    print("\nAvailable categories:\n")
    for cat in categories:
        print(f"{cat['id']:>3}) {cat['name']}")

def select_question_count():
    while True:
        try:
            count = int(input("\nHow many questions do you want? (1-50): "))
            if 1 <= count <= 50:
                return count
            else:
                print(" Please enter a number between 1 and 50.")
        except ValueError:
            print(" Please enter a valid number.")




