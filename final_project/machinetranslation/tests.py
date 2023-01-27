import unittest
from translator import english_to_french, french_to_english

class TestEnglishTranslator(unittest.TestCase):
    def test_english_to_french1(self):
        self.assertEqual(english_to_french(""),"Please enter a valid English word")
    def test_english_to_french2(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test_english_to_french3(self):
        self.assertEqual(english_to_french("Goodbye"),"Au revoir")
    def test_english_to_french4(self):
        self.assertNotEqual(english_to_french("Goodbye"),"Bonjour")

class TestFrenchTranslator(unittest.TestCase):
    def test_french_to_english1(self):
        self.assertEqual(french_to_english(""),"Entrez un mot français valide")
    def test_french_to_english2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    def test_french_to_english3(self):
        self.assertEqual(french_to_english("Au revoir"),"Goodbye")
    def test_french_to_english4(self):
        self.assertNotEqual(french_to_english("Bonjour"),"Goodbye")

unittest.main()