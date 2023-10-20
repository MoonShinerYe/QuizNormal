
import unittest
from tkinter import filedialog
from unittest.mock import patch, MagicMock
from main import SurveyApplication

class TestSurveyApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = SurveyApplication()
        cls.app.open_file_flag = True

    def test_open_file(self):
        with patch('tkinter.filedialog.askopenfilename') as mock_askopenfilename:
            mock_askopenfilename.return_value = "sample.txt"
            self.app.open_file()
            self.assertEqual(self.app.filepath, "sample.txt")

    def test_loadbackground(self):
        self.app.loadbackground()
        self.assertIsNotNone(self.app.background_img)

    def test_show_title(self):
        self.app.title_entry = MagicMock()
        self.app.submit_title_btn = MagicMock()
        self.app.title_img_label = MagicMock()
        self.app.txtlbl = MagicMock()
        self.app.create_widgets = MagicMock()

        self.app.show_title()

        self.assertEqual(self.app.title_label["text"], self.app.title_entry.get())
        self.assertTrue(self.app.title_entry.pack_forget.called)
        self.assertTrue(self.app.submit_title_btn.pack_forget.called)
        self.assertTrue(self.app.title_img_label.pack_forget.called)
        self.assertTrue(self.app.txtlbl.pack_forget.called)
        self.assertTrue(self.app.create_widgets.called)

    def test_title_quiz(self):
        self.app.title_label = MagicMock()
        self.app.title_entry = MagicMock()
        self.app.submit_title_btn = MagicMock()
        self.app.title_picture_add = MagicMock()

        self.app.title_quiz()

        self.assertTrue(self.app.title_label.pack.called)
        self.assertTrue(self.app.title_entry.pack.called)
        self.assertTrue(self.app.submit_title_btn.pack.called)
        self.assertTrue(self.app.title_picture_add.called)

    def test_title_picture_add(self):
        self.app.title_img = MagicMock()
        self.app.title_img_label = MagicMock()

        self.app.title_picture_add()

        self.assertTrue(self.app.title_img_label.pack.called)

    def test_create_widgets(self):
        self.app.question_label = MagicMock()
        self.app.question_entry = MagicMock()
        self.app.answer_label = MagicMock()

        self.app.create_widgets()

        self.assertTrue(self.app.question_label.pack.called)
        self.assertTrue(self.app.question_entry.pack.called)
        self.assertTrue(self.app.answer_label.pack.called)
    
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