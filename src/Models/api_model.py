import requests

BASE_URL = "https://opentdb.com/api.php"
CATEGORY_URL = "https://opentdb.com/api_category.php"

def get_categories():
    response = requests.get(CATEGORY_URL)
    if response.status_code == 200:
        return response.json().get("trivia_categories", [])
    return []

def get_questions(amount=10, category=None, difficulty=None):
    params = {"amount": amount, "type": "multiple"}
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
