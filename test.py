
import unittest
import tkinter as tk
from main import SurveyApplication

class TestSurveyApplication(unittest.TestCase):
    def setUp(self):
        self.app = SurveyApplication()
        self.app.open_file_flag = False

    def test_show_result_correct(self):
        self.app.open_file_flag = False
        self.app.questions = [{'question': 'Question 1', 'answer': 'Answer 1'}]
        self.app.question_index = 0
        self.app.show_result(True)
        result_label = self.app.winfo_children()[-1]  # Get the last label widget added to the application
        expected_text = "1. Вопрос: Question 1 Ответ: Answer 1. Верно!"
        self.assertEqual(result_label["text"], expected_text)

    def test_show_result_incorrect(self):
        self.app.open_file_flag = True
        self.app.questions_txt = [['Question 1', 'Answer 1']]
        self.app.question_num = 1
        self.app.show_result(False)
        result_label = self.app.winfo_children()[-1]  # Get the last label widget added to the application
        expected_text = "1. Вопрос: Question 1 Ответ: Answer 1. Неверно!"
        self.assertEqual(result_label["text"], expected_text)

if __name__ == '__main__':
    unittest.main()