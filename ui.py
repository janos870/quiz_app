from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

   def __init__(self, quize_brain: QuizBrain):
       self.quiz = quize_brain
       self.window = Tk()
       self.window.title("Quizzler")
       self.window.config(bg=THEME_COLOR, padx=20, pady=20)

       self.score_label = Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR)
       self.score_label.grid(row=0, column=1)

       self.canvas = Canvas(width=400, height=250, bg="white", highlightthickness=0)
       self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

       self.question_text = self.canvas.create_text(
           150, 125,
           width=200,
           text="Question text",
           fill=THEME_COLOR,
           font=("Arial", 20, "bold")
       )

       true_image = PhotoImage(file="images/true.png")
       false_image = PhotoImage(file="images/false.png")

       self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
       self.true_button.grid(row=2, column=0)

       self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
       self.false_button.grid(row=2, column=1)

       self.get_next_question()

       self.window.mainloop()

   def get_next_question(self):
       if self.quiz.still_has_questions():
           self.canvas.config(bg="white")
           self.score_label.config(text=f"Score: {self.quiz.score}")
           q_text = self.quiz.next_question()
           self.canvas.itemconfig(self.question_text, text=q_text)
       else:
           self.canvas.config(bg="white")
           self.score_label.config(text=f"Score: {self.quiz.score}")
           self.canvas.itemconfig(self.question_text, text="All done!")
           self.true_button.config(state="disabled")
           self.false_button.config(state="disabled")

   def true_pressed(self):
       self.feedback(self.quiz.check_answer("True"))

   def false_pressed(self):
       is_right = self.quiz.check_answer("False")
       self.feedback(is_right)

   def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






