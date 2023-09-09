from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizller")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)


        self.label=Label(text="Score:0",fg="white",bg=THEME_COLOR,font=("Arial",20))
        self.label.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Some question text", fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(column=0,row=1,columnspan=4,pady=50)


        self.option1 = Button(text="1",width=5,command=self.option1_click)
        self.option1.grid(row=2, column=0)

        self.option2 = Button(text="2",width=5,command=self.option2_click)
        self.option2.grid(row=2, column=1)

        self.option3 = Button(text="3",width=5,command=self.option3_click)
        self.option3.grid(row=2, column=2)

        self.option4 = Button(text="4",width=5,command=self.option4_click)
        self.option4.grid(row=2, column=3)


        self.get_next_question()

        self.window.mainloop()
    def option1_click(self):
        self.give_feedback(self.quiz.check_answer(1))
    def option2_click(self):
        self.give_feedback(self.quiz.check_answer(2))
    def option3_click(self):
        self.give_feedback(self.quiz.check_answer(3))
    def option4_click(self):
        self.give_feedback(self.quiz.check_answer(4))

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text,fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text,text="you have reached the end of the quiz",fill=THEME_COLOR)
            self.option1.config(state="disabled")
            self.option2.config(state="disabled")
            self.option3.config(state="disabled")
            self.option4.config(state="disabled")

    def give_feedback(self,is_right):
        self.canvas.itemconfig(self.question_text, text=f"the correct answer is {self.quiz.current_question.answer}",fill="white")
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)








