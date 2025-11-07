import requests

import requests

def get_questions(amount=10, difficulty="easy"):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "type": "multiple",
        "difficulty": difficulty
    }
    response = requests.get(url, params=params)
    return response.json()["results"]
