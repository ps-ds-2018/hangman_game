# Hangman Game - Flight Safety Edition

## Project Overview
This project implements a **Hangman Game AI** that can play Hangman efficiently, aiming to guess words **within 6 incorrect attempts**. The word list consists of **100 flight safety-related terms**.

## 🚀 Features
- Receives repeated inputs of the **current word state** and **letters guessed so far**.
- Outputs a **single letter guess** per turn until the word is guessed or attempts run out.
- Implements **manual gameplay** (`game.py`) and **automated testing** (`test_hangman.py`).
- Supports **future API integration** for external calls.

## 📂 Project Structure
```
hangman_game/
│── hangman/
│   │── __init__.py            # Marks the folder as a package
│   │── game.py                # Main Hangman game (manual play)
│   │── logic.py               # Core game logic (letter selection, word updates)
│   │── utils.py               # Helper functions (word processing, display)
│── tests/
│   │── __init__.py            # Marks the folder as a package
│   │── test_hangman.py        # Automated testing script
│── words.txt                  # 100 flight safety-related words
│── requirements.txt           # Required Python dependencies
│── README.md                  # Project Documentation (this file)
│── .gitignore                 # Excludes unnecessary files
```

## Installation & Setup
### **1️. Clone the Repository**
```bash
git clone https://github.com/ps-ds-2018/hangman_game.git
cd hangman_game
```

### **2️. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows
```

### **3️. Install Dependencies**
```bash
pip install -r requirements.txt
```

## Running the Hangman Game (Manual Mode)
To play manually:
```bash
python hangman/game.py
```

## Running Automated Tests (AI vs. 100 Words)
```bash
python tests/test_hangman.py
```

## 🔍 How It Works
1. **Word Selection**: Picks a word from `words.txt`.
2. **Letter Guessing Strategy**:
   - Uses **letter frequency** analysis to make educated guesses.
   - Prioritizes vowels early, then moves to common consonants.
   - Avoids repeating guessed letters.
3. **Game Progression**:
   - Updates the word state after each guess.
   - Tracks incorrect attempts (max **6 mistakes** allowed).
   - Displays Hangman figure as mistakes increase.
   - Ends when the word is guessed or all attempts are used.



## Author
Developed by **Priya Saxena**. Contributions & feedback welcome!



