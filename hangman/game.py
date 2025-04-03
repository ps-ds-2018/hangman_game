from hangman.utils import find_idx, replace_chars_at_indices
from hangman.display import print_hangman

def play_hangman(word):
    masked_word = "_" * len(word)
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    print("Length of the word to guess:", len(word))
    print(" ".join(masked_word))

    while incorrect_guesses < max_guesses and masked_word != word:
        user_input = input("Make a guess: ").lower()

        if user_input in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(user_input)

        if user_input in word:
            print("That's correct!")
            indices = find_idx(word, user_input)
            masked_word = replace_chars_at_indices(masked_word, indices, user_input)
        else:
            print("That's incorrect.")
            incorrect_guesses += 1
            print_hangman(incorrect_guesses)

        print("currentWordState:", " ".join(masked_word))
        print("remainingGuesses:", max_guesses - incorrect_guesses)
        print("guessedLettersSoFar:", guessed_letters)

    if masked_word == word:
        print("Word Complete. Congratulations! You survived.")
    else:
        print("Game over! The word was:", word)
