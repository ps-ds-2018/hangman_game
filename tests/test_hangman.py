import unittest
from hangman.logic import process_guess

class TestHangman(unittest.TestCase):
    def test_correct_guess(self):
        word = "pilot"
        masked_word = "_ _ _ _ _"
        guessed_letters = []
        remaining_guesses = 6

        new_masked, guessed, remaining, msg = process_guess(word, "p", masked_word, guessed_letters, remaining_guesses)
        self.assertIn("p", new_masked)
        self.assertEqual(msg, "Correct guess!")

    def test_wrong_guess(self):
        word = "pilot"
        masked_word = "_ _ _ _ _"
        guessed_letters = []
        remaining_guesses = 6

        new_masked, guessed, remaining, msg = process_guess(word, "z", masked_word, guessed_letters, remaining_guesses)
        self.assertEqual(remaining, 5)
        self.assertEqual(msg, "Wrong guess!")

if __name__ == "__main__":
    unittest.main()
