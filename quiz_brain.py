import html
class QuizBrain:
    def __init__(self,q_list):
        self.q_number=0
        self.score=0
        self.list=q_list

    def next_question(self):
        self.current_question=self.list[self.q_number]
        q_text=html.unescape(self.current_question.text)
        q_answer = html.unescape(self.current_question.answer)

        q_options = self.current_question.options
        self.q_number += 1
        return f"Q.{self.q_number}:{q_text} \n" \
               f"1.{q_options[0]}\n" \
               f"2.{q_options[1]}\n" \
               f"3.{q_options[2]}\n" \
               f"4.{q_options[3]}\n"


        # self.check_answer(user_answer,q_option,q_answer)
    def still_has_questions(self):
        return self.q_number<len(self.list)

    def check_answer(self, user_answer:int)->bool:
        correct_answer = self.current_question.ans_no
        if user_answer == int(correct_answer)+1:
            self.score += 1
            return True
        else:
            return False



