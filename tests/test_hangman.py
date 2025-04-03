import random
from tests.auto_game import auto_play_hangman

def load_words(filename):
    """Load words from a file into a list."""
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def generate_guess_list():
    """Generate a shuffled list of all letters to simulate random guessing."""
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    return letters

def test_all_words(words):
    """Test Hangman on all words in the list."""
    successes = 0

    for word in words:
        guess_list = generate_guess_list()
        success, guessed_letters = auto_play_hangman(word, guess_list)

        if success:
            print(f"✅ Successfully guessed '{word}' with guesses: {guessed_letters}")
            successes += 1
        else:
            print(f"❌ Failed to guess '{word}'. Guessed: {guessed_letters}")

    print(f"\nFinished testing. Success rate: {successes}/{len(words)} words guessed correctly.")

if __name__ == "__main__":
    words = load_words("words.txt")
    test_all_words(words)
