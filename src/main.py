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

        choice = input("\nChoose an option (1–4): ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            custom_quiz()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\n Invalid choice. Please enter a number between 1 and 4.")
            input("Press ENTER to try again...")

if __name__ == "__main__":
    main()
