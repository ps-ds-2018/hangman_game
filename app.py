from flask import Flask, render_template, request, jsonify
import random
from hangman.logic import get_next_guess, initialize_game, process_guess

app = Flask(__name__)

# Load words from words.txt
with open("words.txt", "r") as f:
    WORDS = [line.strip() for line in f.readlines()]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/start-game", methods=["POST"])
def start_game():
    word = random.choice(WORDS).upper()
    masked_word, guessed_letters, remaining_guesses = initialize_game(word)
    return jsonify({
        "word": word,
        "maskedWord": masked_word,
        "guessedLetters": guessed_letters,
        "remainingGuesses": remaining_guesses
    })

@app.route("/make-guess", methods=["POST"])
def make_guess():
    data = request.get_json()
    word = data["word"]
    guessed_letter = data["letter"].upper()
    masked_word = data["maskedWord"]
    guessed_letters = data["guessedLetters"]
    remaining_guesses = data["remainingGuesses"]

    new_masked_word, guessed_letters, remaining_guesses, message = process_guess(
        word, guessed_letter, masked_word, guessed_letters, remaining_guesses
    )

    return jsonify({
        "maskedWord": new_masked_word,
        "guessedLetters": guessed_letters,
        "remainingGuesses": remaining_guesses,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True)
