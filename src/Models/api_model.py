import requests

import requests

def get_questions(amount=10, category=None, difficulty=None):
    
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "type": "multiple"
    }


    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty

    response = requests.get(url, params=params)
    data = response.json()


    if data.get("response_code") != 0:
        print(" No questions found for this configuration.")
        return []

    return data.get("results", [])



def get_categories():

    url = "https://opentdb.com/api_category.php"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["trivia_categories"]
    except requests.RequestException:
        return []
