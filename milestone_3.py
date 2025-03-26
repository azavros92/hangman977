# milestone_3.py

import random

# Select a random word from a predefined list
def get_random_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(word_list)

# Check if the guessed letter is in the secret word
def check_guess(guess, secret_word):
    guess = guess.lower()  # Ensure consistency by converting to lowercase
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Get a valid letter input from the user
def get_user_guess():
    while True:
        guess = input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess  # Return the valid guess instead of breaking the loop
        print("Invalid letter. Please enter a single alphabetical character.")

# Main function to run the game logic
def play_hangman():
    secret_word = get_random_word()  # Get a random word
    guess = get_user_guess()  # Get user input
    check_guess(guess, secret_word)  # Check if the guess is correct

# Run the game
if __name__ == "__main__":
    play_hangman()