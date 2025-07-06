class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        if self.check_answer(input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?\n")):
            print("That is correct!")
        else:
            print("That is incorrect.")
        self.question_number += 1

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True
