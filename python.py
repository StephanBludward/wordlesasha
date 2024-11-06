import random
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# List of potential words
words = ["apple", "grape", "peach", "melon", "lemon"]

# Choose a random word from the list
target_word = random.choice(words)
attempts = 6

# Welcome message and instructions
print(" Welcome to the game!")
print("Guess the 5-letter word within 6 attempts.\n")
print(f"{Fore.GREEN}G{Style.RESET_ALL}: Correct letter in the correct position")
print(f"{Fore.YELLOW}Y{Style.RESET_ALL}: Correct letter in the wrong position")
print(f"-: Letter not in the word at all\n")

# Game loop
for attempt in range(attempts):
    guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()

    # Ensure guess is exactly 5 letters
    if len(guess) != 5:
        print("Enter a 5-letter word.")
        continue

    # Feedback variable for each letter
    feedback = ""
    
    # Check each letter in the guess
    for i in range(5):
        if guess[i] == target_word[i]:
            feedback += f"{Fore.GREEN}{guess[i].upper()}{Style.RESET_ALL}"  # Correct position
        elif guess[i] in target_word:
            feedback += f"{Fore.YELLOW}{guess[i].upper()}{Style.RESET_ALL}"  # Wrong position
        else:
            feedback += f"{guess[i].upper()}"  # Not in word
    
    print("Feedback:", feedback)  # Show formatted feedback

    # Check if the guess is correct
    if guess == target_word:
        print(f"\nCongratulations! You've guessed the word '{target_word.upper()}' correctly! 🎉")
        break
else:
    print(f"\You've used all attempts. The word was: {target_word.upper()}")
