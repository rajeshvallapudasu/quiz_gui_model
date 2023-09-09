import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank=[]



for question in question_data:
    question["incorrect_answers"].append(question["correct_answer"])
    random.shuffle(question["incorrect_answers"])
    new_answer_no = question["incorrect_answers"].index(question["correct_answer"])
    new_question_text=question["question"]
    new_question_options=question["incorrect_answers"]
    new_question_answer=question["correct_answer"]
    new_q=Question(new_question_text,new_question_options,new_question_answer,new_answer_no)
    question_bank.append(new_q)
quiz=QuizBrain(question_bank)
quiz_interface=QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()
# print(f"quiz completed, your final score is {quiz.score}/{len(question_bank)}")