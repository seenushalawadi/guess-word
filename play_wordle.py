🎮 Terminal Wordle Game (Python)

A simple Wordle-style terminal game written in Python.
The player has to guess a secret word within a limited number of attempts. After each guess, the game provides color-coded feedback to indicate correct letters and positions.

This project runs entirely in the command line and uses colored output for a better gameplay experience.

📌 Features

🎯 Random secret word selection

⌨️ User input validation

🟩 Green letters for correct position

🟨 Yellow letters for correct letter in wrong position

⬜ White letters for incorrect letters

🔢 Limited number of attempts

📦 Word list loaded from a file

🖥️ Clean terminal UI with borders

               🧠 Game Clue
A girl with a man about to start a new life

Use the clue to help guess the secret word.

                📂 Project Structure
project-folder/
│
├── main.py
├── wordle.py
├── letter_state.py
│
├── data/
│   └── wordle_words.txt
│
└── README.md

⚙️ Installation

Clone the repository
git clone https://github.com/your-username/terminal-wordle.git

cd guess-word

run python play_wordle.py

🎮 How to Play

Enter a 5-letter word.

After each guess, the game shows colored feedback:

| Color     | Meaning                            |
| --------- | ---------------------------------- |
| 🟩 Green  | Correct letter in correct position |
| 🟨 Yellow | Correct letter but wrong position  |
| ⬜ White   | Letter not in the word             |


🧾 Example Gameplay
                
Clue: --- A girl with a man about to start a new life ---

Type your guess: PLANT

Your results so far...
You have 5 attempts remaining.

┌─────────────┐
│ P L A N T   │
│ _ _ _ _ _   │
│ _ _ _ _ _   │
│ _ _ _ _ _   │
│ _ _ _ _ _   │
│ _ _ _ _ _   │
└─────────────┘
