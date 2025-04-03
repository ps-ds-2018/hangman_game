import string
from collections import Counter

def get_next_guess(current_word_state: str, guessed_letters: list):
    """
    Determines the next letter to guess based on the current state of the word.
    :param current_word_state: String representing the masked word (e.g., '_ _ e _ a n')
    :param guessed_letters: List of letters already guessed
    :return: A single character representing the next guess
    """
    # Convert masked word into a set of missing characters
    missing_chars = set(current_word_state.replace(" ", "")) - set(guessed_letters)
    
    # If missing_chars exist, try to guess a common letter
    if missing_chars:
        letter_frequencies = Counter("etaoinsrhdlucmfywgpbvkxqjz")  # Common letter order
        for letter, _ in letter_frequencies.most_common():
            if letter not in guessed_letters:
                return letter
    
    # Default to any unused letter if no pattern match is found
    for letter in string.ascii_lowercase:
        if letter not in guessed_letters:
            return letter
    
    return None  # No more guesses possible
