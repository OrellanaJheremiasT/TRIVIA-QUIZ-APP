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
