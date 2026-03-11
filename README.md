# guess-word
Developed a console-based word guessing game with core gameplay features to select random words 
accept user guesses, track attempts, and display progress using string manipulation.

🎮 Guess The Word Game (Python)

A simple command-line word guessing game written in Python.
The player tries to guess a hidden word one letter at a time within a limited number of attempts.

If the player guesses all the letters before the attempts run out, they win the game. Otherwise, 
the game ends and the correct word is revealed.

________________________________________
📌 Features
Interactive terminal-based gameplay Guess the word 
one letter at a time Maximum of 10 attempts 
Displays the current word progress Validates 
user input Shows win or game-over message

📂 Project Structure
guess-the-word/
│
├── main.py          # Main game logic (GuessTheWord class)

├── words.py         # Handles word selection and guessing logic

└── README.md        # Project documentation
________________________________________

⚙️ Requirements
Python 3.7+
No external libraries are required.

▶️ How to Run
Clone or download the repository.
git clone https://github.com/seenushalawadi/guess-word.git

Navigate to the project folder.
cd guess-the-word

Run the game.
python main.py
--------------------------------------------------------------------------
🎯 How the Game Works
The game selects a random hidden word using the Words class.
The player guesses one letter at a time.
If the letter exists in the word:
The correct positions are revealed.
If the guess is incorrect:
One attempt is deducted.
The game ends when:
The player guesses the entire word, or
The player runs out of attempts.
--------------------------------------------------------------------------
🧠 Code Overview
GuessTheWord Class
Handles the main gameplay logic.

Methods
__init__()  Initializes the game with: Maximum attempts (10) Word object 

start() Runs the main game loop and controls gameplay.

get_input() Validates and returns a single letter guessed by the user.

Words Class (from words.py)

Responsible for managing the hidden word.

Typical responsibilities include:
Selecting a random word
Tracking guessed letters
Updating displayed word progress
Checking if the word is fully guessed
--------------------------------------------------------------------------

💡 Example Gameplay
🎮 Welcome to 'Guess the Word' game!

Word: _ _ _ _ _
Tries left: 10
Enter a letter to guess the word: a

❌ Oops! 'a' is not in the word.

Word: _ _ _ _ _
Tries left: 9
Enter a letter to guess the word: e

✅ Good job! 'e' is correct.
🚀 Possible Improvements
--------------------------------------------------------------------------
Add difficulty levels 
Show already guessed letters
Add ASCII hangman graphics
Load words from a dictionary file
Add GUI using Tkinter or PyQt
Track player score
