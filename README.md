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


🛠️ Technologies Used

Python

Colorama – for colored terminal text

Random module – for secret word selection

📂 Project Structure

project-folder/

├── main.py

├── wordle.py

├── letter_state.py

├── data/

└── wordle_words.txt

└── README.md




⚙️ Installation

Clone the repository

git clone https://github.com/seenushalawadi/guess-word.git

Navigate into the project

cd guess-word


▶️ How to Run

Run the game using:

python  play_wordle.py


🎮 How to Play

Enter a 5-letter word.

After each guess, the game shows colored feedback:

Color	Meaning
🟩 Green	Correct letter in correct position
🟨 Yellow	Correct letter but wrong position
⬜ White	Letter not in the word

Keep guessing until you solve the puzzle or run out of attempts.

<img width="359" height="426" alt="image" src="https://github.com/user-attachments/assets/18fba2c1-c76a-4d8d-9344-15bc381b0905" />



  thankyou..........
