import unittest
import hangman_lexicon as hl
import main

class TestHangmanLexicon(unittest.TestCase):

    def test_hangman_class(self):
        lexicon = hl.HangmanLexicon()
        self.assertTrue(lexicon.size() > 0)
        self.assertTrue(lexicon.get_word(lexicon.size()) is None)
        self.assertTrue(lexicon.get_word(0) is not None)

    def test_update_guessed_word(self):
        cases = [
            ("NITWIT",["-","-","-","-","-","-"],"I",["-","I","-","-","I","-"])
        ]
        for case in cases:
            self.assertTrue(main.update_guessed_word(case[0],case[1],case[2]) == case[3])

if __name__ == '__main__':
    unittest.main()
