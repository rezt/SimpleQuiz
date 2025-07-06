from question_model import Question
from quiz_brain import QuizBrain
import requests
import json

question_bank = []

r = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=hard&type=boolean")
api_data = json.loads(r.content)

for i in api_data["results"]:
    question_bank.append(Question(i["question"],i["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score: {quiz.score}/{quiz.question_number}")
