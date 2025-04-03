from hangman.utils import find_idx, replace_chars_at_indices
from hangman.display import print_hangman

def auto_play_hangman(word, guess_list):
    """Automatically plays Hangman using a predefined list of guesses."""
    masked_word = "_" * len(word)
    guessed_letters = set()
    incorrect_guesses = 0

    for guess in guess_list:
        if guess in guessed_letters:
            continue

        guessed_letters.add(guess)

        if guess in word:
            indices = find_idx(word, guess)
            masked_word = replace_chars_at_indices(masked_word, indices, guess)
        else:
            incorrect_guesses += 1
            print_hangman(incorrect_guesses)

        if masked_word == word:
            return True, guessed_letters  # Successfully guessed the word

        if incorrect_guesses >= 6:
            return False, guessed_letters  # Game lost

    return False, guessed_letters  # If guesses run out before solving
