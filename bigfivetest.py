import tkinter as tk
from tkinter import messagebox
class BigFiveTest:
    def __init__(self):
        self.questions = [
            "Question 1",
            "Question 2",
            # Add more questions...
        ]
        self.answers = []
    def start(self):
        self.current_question = 0
        self.create_question_window()
    def create_question_window(self):
        self.question_window = tk.Toplevel()
        self.question_window.title("Question")
        self.question_label = tk.Label(self.question_window, text=self.questions[self.current_question])
        self.question_label.pack(pady=20)
        self.yes_button = tk.Button(self.question_window, text="Yes", command=self.answer_yes)
        self.yes_button.pack(pady=10)
        self.no_button = tk.Button(self.question_window, text="No", command=self.answer_no)
        self.no_button.pack(pady=10)
    def answer_yes(self):
        self.answers.append(1)
        self.next_question()
    def answer_no(self):
        self.answers.append(0)
        self.next_question()
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
        else:
            self.show_result()
    def show_result(self):
        # Calculate and display the result
        score = sum(self.answers)
        result = messagebox.showinfo("Result", f"Your score is {score} out of {len(self.questions)}")
