from Controllers.quiz_controller import run_quiz, custom_quiz
from views.ui import clear, banner
import time

def main_menu():
    while True:
        clear()
        banner()
        print("1) Quick Mode (30 random questions)")
        print("2) Custom Quiz (choose everything)")
        print("3) Exit")
        
        option = input("\nSelect an option: ")
        if option == "1":
            run_quiz()
        elif option == "2":
            custom_quiz()
        elif option == "3":
            print("👋 See you next time!")
            time.sleep(1)
            break
        else:
            print(" Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()

if __name__ == "__main__":
    run_quiz()