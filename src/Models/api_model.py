import requests

def get_questions(amount=10):
    url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple"}
    response = requests.get(url, params=params)
    return response.json()["results"]