from question_model import Question
from quiz_brain import QuizBrain
import trivia_api
import art

question_bank = []

print(art.logo)

try: number_of_questions = int(input("How many questions do you want?\n"))
except ValueError:
    number_of_questions = 1
if number_of_questions > 50:
    number_of_questions = 50

selected_difficulty = input("Select difficulty: easy/medium/hard\n").lower()

if selected_difficulty not in ["easy", "medium", "hard"]:
    api_data = trivia_api.get_quiz(number_of_questions, "easy")
else:
    api_data = trivia_api.get_quiz(number_of_questions,selected_difficulty)

for i in api_data["results"]:
    text = i["question"]
    text = text.replace("&quot;","")
    text = text.replace("&#039;", "")
    question_bank.append(Question(text,i["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score: {quiz.score}/{quiz.question_number}")
