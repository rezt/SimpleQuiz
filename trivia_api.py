import requests
import json

def get_quiz(number_of_questions = 0, difficulty = "easy"):
    s = f"https://opentdb.com/api.php?amount={number_of_questions}&category=15&difficulty={difficulty}&type=boolean"
    r = requests.get(s)
    return json.loads(r.content)
