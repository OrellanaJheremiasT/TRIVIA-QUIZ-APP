from Models.supabase_model import get_all_players
from views.ui import clear, banner

def show_stats():
    clear()
    banner()
    print("=== PLAYER STATISTICS ===\n")

    players = get_all_players()

    if not players:
        print("No player data found.")
        input("\nPress ENTER to return to the menu...")
        return

    print(f"{'Player':<15}{'Score':<10}{'Questions':<12}{'Difficulty':<12}{'Date':<20}")
    print("-" * 70)

    for p in players:
        print(f"{p['name']:<15}{p['score']:<10}{p['total_questions']:<12}{p['difficulty']:<12}{p['date_played'][:19]:<20}")

    input("\nPress ENTER to return to the menu...")
