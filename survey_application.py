import tkinter as tk
from tkinter import filedialog

class SurveyApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "QuizRunner"
        self.resizable = False
        self.questions = []

    def open_file(self):
        filepath = filedialog.askopenfilename()
        # Code to parse the file and populate the questions list
        pass

    def load_background(self):
        # Code to load and display the background image
        pass

    def show_title(self):
        # Code to update the UI with the entered title
        pass

    def create_widgets(self):
        # Code to create UI widgets
        pass

    def add_question(self):
        question_text = self.question_entry.get()
        answer_text = self.answer_entry.get()
        question = {'question': question_text, 'answer': answer_text}
        self.questions.append(question)

if __name__ == '__main__':
    app = SurveyApplication()
    app.mainloop()