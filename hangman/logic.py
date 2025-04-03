import random

def get_next_guess(current_word_state, guessed_letters):
    # Simple strategy: choose a random letter that hasn't been guessed
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    possible_choices = [letter for letter in alphabet if letter not in guessed_letters]

    return random.choice(possible_choices) if possible_choices else None

def initialize_game(word):
    return "_ " * len(word), [], 6

def process_guess(word, guessed_letter, masked_word, guessed_letters, remaining_guesses):
    if guessed_letter in guessed_letters:
        return masked_word, guessed_letters, remaining_guesses, "Letter already guessed."

    guessed_letters.append(guessed_letter)

    if guessed_letter in word:
        new_masked_word = "".join(
            guessed_letter if word[i] == guessed_letter else masked_word[i]
            for i in range(len(word))
        )
        return new_masked_word, guessed_letters, remaining_guesses, "Correct guess!"
    else:
        remaining_guesses -= 1
        return masked_word, guessed_letters, remaining_guesses, "Wrong guess!"
