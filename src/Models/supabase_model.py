from supabase import create_client
import os
from dotenv import load_dotenv
from datetime import datetime

env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=env_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception(" Missing SUPABASE_URL or SUPABASE_KEY in .env file")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_player(name, score, total_questions, difficulty):

    data = {
        "name": name,
        "score": score,
        "total_questions": total_questions,
        "difficulty": difficulty,
        "date_played": datetime.now().isoformat()
    }
    supabase.table("players").insert(data).execute()

def get_all_players():

    response = supabase.table("players").select("*").order("date_played", desc=True).execute()
    return response.data
