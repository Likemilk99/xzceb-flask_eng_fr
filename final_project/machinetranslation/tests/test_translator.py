import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test_englishToFrenchIsNull(self):
        self.assertIsNone(englishToFrench(None))

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglishIsNull(self):
        self.assertIsNone(frenchToEnglish(None))

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
