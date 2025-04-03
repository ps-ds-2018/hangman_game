from flask import Flask, request, jsonify
from hangman.logic import get_next_guess  # Import logic function

app = Flask(__name__)

@app.route('/hangman/guess', methods=['POST'])
def get_guess():
    data = request.get_json()
    
    current_word_state = data.get("currentWordState", "")
    guessed_letters = data.get("guessedLetters", [])
    guesses_remaining = data.get("guessesRemaining", 6)
    
    if not current_word_state:
        return jsonify({"error": "Invalid input. Missing currentWordState."}), 400
    
    next_guess = get_next_guess(current_word_state, guessed_letters)
    
    return jsonify({"nextGuess": next_guess})

if __name__ == '__main__':
    app.run(debug=True)
