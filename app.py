from flask import Flask, render_template, request, session
import random
from hangman.logic import get_next_guess

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

# Load words from file
with open("words.txt", "r") as f:
    WORD_LIST = [line.strip() for line in f.readlines()]

@app.route("/")
def home():
    session["word"] = random.choice(WORD_LIST).lower()
    session["masked_word"] = "_" * len(session["word"])
    session["guessed_letters"] = []
    session["guesses_remaining"] = 6
    return render_template("index.html", masked_word=session["masked_word"], guessed_letters=[], remaining=session["guesses_remaining"])

@app.route("/guess", methods=["POST"])
def guess():
    if session["guesses_remaining"] > 0:
        letter = request.form.get("letter").lower()
        
        if letter in session["guessed_letters"]:
            message = "You've already guessed that letter!"
        else:
            session["guessed_letters"].append(letter)

            if letter in session["word"]:
                indices = [i for i, c in enumerate(session["word"]) if c == letter]
                masked_word_list = list(session["masked_word"])
                for idx in indices:
                    masked_word_list[idx] = letter
                session["masked_word"] = "".join(masked_word_list)
                message = "Correct!"
            else:
                session["guesses_remaining"] -= 1
                message = "Incorrect guess."

        if "_" not in session["masked_word"]:
            message = "Congratulations! You guessed the word."

        return render_template("index.html", masked_word=session["masked_word"], guessed_letters=session["guessed_letters"], remaining=session["guesses_remaining"], message=message)

    return render_template("index.html", masked_word=session["masked_word"], guessed_letters=session["guessed_letters"], remaining=session["guesses_remaining"], message="Game Over!")

if __name__ == "__main__":
    app.run(debug=True)
