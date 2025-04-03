# **Flight Safety Hangman Game** 

A **Flask-based Hangman game** designed to test and improve **flight safety knowledge**. The game challenges players to guess aviation-related words within **6 incorrect attempts** before the Hangman figure is fully drawn.  

---

## **Project Overview**  
This project implements a **web-based Hangman game** that can be played manually through a **Flask-powered web interface**. The word list consists of **100 flight safety-related terms**.  


### **Features**  
**Interactive Web UI** – Built with **HTML, CSS, and JavaScript**.  
**Flask Backend** – Manages game logic and API calls.  
**Real-time Gameplay** – Tracks **guessed letters**, **remaining attempts**, and **hangman figure**.  
**Letter Guessing Strategy** – Encourages smart guessing based on **letter frequency analysis**.  
**Restart & Navigation** – Allows restarting the game or returning to the landing page.  

---

## **Tools & Technologies Used**  
- **Flask (Python)** – Backend server handling game logic & API responses.  
- **HTML, CSS, JavaScript** – Frontend UI for a seamless game experience.  
- **AJAX (Fetch API)** – Enables real-time updates without page refresh.  
- **Python (Game Logic)** – Implements Hangman rules, word selection, and game progress.  

---

## **How the Game Works**  

### **Gameplay**  
1️. The game randomly selects a **word** from a **100-word aviation safety list**.  
2️. The word is displayed as **underscores** (_ _ _ _), one for each letter.  
3️. Players **input a letter** to make a guess.  
4️. If the guess is **correct**, the letter is revealed in the word.  
5️. If the guess is **incorrect**, the **hangman drawing** progresses.  
6️. The player **wins** if they guess the word before the hangman is fully drawn.  
7️. The player **loses** after **6 incorrect guesses**.  


### **Game Interface**  
- **Displays:**  
  - **Word Length**  
  - **Masked Word**  
  - **Guessed Letters**  
  - **Remaining Attempts**  
  - **Hangman Drawing**  
- **Buttons:**  
  - **Submit Guess** – Input a letter and check if it's correct.  
  - **Restart Game** – Start a new round with a fresh word.  
  - **Back to Home** – Return to the landing page.  

---

## **Hangman Strategy**  
🔹 **Start with vowels** (A, E, I, O, U) – These are more frequent in words.  
🔹 **Move to common consonants** (R, S, T, L, N, D).  
🔹 **Look for familiar patterns** like **TH, CH, SH, ING, ED**.  
🔹 **Avoid repeating letters** – Keep track of previous guesses.  
🔹 **Use elimination** – Deduce unknown letters based on known patterns.  

---

## Project Structure  

hangman_game/  
│── hangman/                        # Core game logic  
│   │── __init__.py                 
│   │── game.py                     # Manual Hangman game  
│   │── logic.py                    # AI guessing logic  
│   │── utils.py                    # Helper functions  
│   │── display.py                  # Hangman display function  
│  
│── static/                         # CSS & images  
│   │── style.css                   # Styling for landing & game pages  
│   │── landingpage_background.jpg  # Background image for home page  
│   │── header_footer_image.jpg     # Image used in header/footer  
│   │── header-image.jpg            # Image used in header  
│   │── footer-image.jpg            # Image used in footer  
│   │── script.js                   # Frontend JavaScript file  
│   │── style.css                   # Frontend style guide  
│  
│── templates/                      # HTML files for UI  
│   │── index.html                  # Landing page  
│   │── game.html                   # Game page  
│  
│── tests/                          # Testing framework  
│   │── __init__.py         
│   │── test_hangman.py             # Automated testing  
│   │── auto_game.py                # Automated game logic  
│  
│── words.txt                       # 100 flight safety-related words  
│── app.py                          # Flask application  
│── requirements.txt                # Required dependencies  
│── README.md                       # Project documentation (this file)  
│── .gitignore                      # Excludes unnecessary files  


## **Installation & Setup**  

### **1️. Clone the Repository**  

git clone https://github.com/ps-ds-2018/hangman_game.git
cd hangman_game


### **2️. Create a Virtual Environment (Optional but Recommended)**

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

### **3️. Install Dependencies**

pip install -r requirements.txt

### **4. Run the Flask App**

python app.py

Open http://127.0.0.1:5000/ in your browser to start the game.

### **Author**

Developed by Priya Saxena. Contributions & feedback are welcome! 

