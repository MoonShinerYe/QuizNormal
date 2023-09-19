import unittest
from tkinter import Tk
from unittest.mock import patch
from io import StringIO
from main import SurveyApplication

class SurveyApplicationTests(unittest.TestCase):

    def setUp(self):
        self.app = SurveyApplication()
        self.app.title("QuizRunner")
        self.app.geometry("500x500")

    def test_init(self):
        self.assertEqual(self.app.title(), "QuizRunner")
        self.assertEqual(self.app.geometry(), "500x500")
        self.assertFalse(self.app.resizable())

    def test_open_file(self):
        with patch('tkinter.filedialog.askopenfilename', return_value='sample.txt'):
            self.app.open_file()
            self.assertEqual(self.app.filepath, 'sample.txt')
            self.assertEqual(len(self.app.questions_txt), 2)


if __name__ == '__main__':
    unittest.main()

input()