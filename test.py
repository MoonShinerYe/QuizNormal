
import unittest
from tkinter import filedialog
from unittest.mock import patch, MagicMock
from survey_application import SurveyApplication

class TestSurveyApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = SurveyApplication()
        cls.app.open_file_flag = 1

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

if __name__ == '__main__':
    unittest.main()
