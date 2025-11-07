import os
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client, Client 

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_player(name: str, score:int, total_questions:int, difficulty: str):
    name = name.strip() if name else "Anonymous"
    difficulty = difficulty or "Unknown"

    if total_questions == 0:
        raise ValueError("Total questions cannot be zero.")
    if score < 0 or score > total_questions:
        raise ValueError("Score must be between 0 and total questions.")
    
    player_data = {
        "name": name,
        "score": score,
        "total_questions": total_questions,
        "difficulty": difficulty,
        "date": datetime.now().isoformat()
    }

    res = supabase.table("players").insert(player_data).execute()

    if res.error:
       print("Error saving player data:", res.error)
    else:
         print("Player data saved successfully.")

def get_all_players():
    res = supabase.table("players").select("*").order("date", desc=True).execute()





