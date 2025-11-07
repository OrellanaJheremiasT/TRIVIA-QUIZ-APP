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
