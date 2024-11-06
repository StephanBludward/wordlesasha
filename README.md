Wordle Clone in Python
This is a simple, terminal-based Wordle clone written in Python. The game challenges players to guess a randomly selected 5-letter word within six attempts. For each guess, players receive feedback on which letters are in the correct position, which letters are in the word but in the wrong position, and which letters are not in the word at all.

Features
6 Attempts: You have up to six attempts to guess the correct word.
Color-coded Feedback:
Green for letters in the correct position.
Yellow for letters in the word but in the wrong position.
Gray for letters not in the word at all.
User-friendly messages to indicate when you've won or used all attempts.
Prerequisites
Python 3: Ensure you have Python 3 installed.
colorama library: This library is used to provide colored feedback in the terminal.
Installation
Clone or Download the Repository

If you’re cloning the repo, use:
bash
Copy code
git clone https://github.com/your-username/wordlesasha.git
Or, simply download the code files.
Install colorama

Run this command in your terminal:
bash
Copy code
pip install colorama
Usage
Run the Game:

In your terminal, navigate to the folder where the script is saved.
Run the script using:
bash
Copy code
python.py
How to Play:

You’ll be prompted to enter a 5-letter word.
The game will provide color-coded feedback for each letter in your guess:
Green (G): Correct letter in the correct position.
Yellow (Y): Correct letter but in the wrong position.
Gray (-): Letter not in the word at all.
You have six attempts to guess the correct word.
Winning and Losing:

If you guess the word within six attempts, you win!
If you use all six attempts without guessing the word, the game will reveal the correct word.
Example Gameplay
plaintext
Copy code
 Welcome to Wordle! 
Guess the 5-letter word within 6 attempts.

G: Correct letter in the correct position
Y: Correct letter in the wrong position
-: Letter not in the word at all

Attempt 1/6: peach
Feedback: YELLOW YELLOW - GREEN -

Attempt 2/6: ...
Contributing
Feel free to fork this repository, make improvements, and submit a pull request!
