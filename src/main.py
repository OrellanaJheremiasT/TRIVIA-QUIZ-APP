from Controllers.quiz_controller import run_quiz, custom_quiz
from Controllers.stats_controller import show_stats
from views.ui import clear, banner

def main():
    while True:
        clear()
        banner()
        print("1. Play Standard Quiz")
        print("2. Play Custom Quiz")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            custom_quiz()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            break
        else:
            input("Invalid choice. Press ENTER to continue...")

if __name__ == "__main__":
    main()
