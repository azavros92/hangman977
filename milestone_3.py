# milestone_3.py

import random

# Step 1: Create a list of words and choose a random word
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
secret_word = random.choice(word_list)

# Step 1: Define the check_guess function
def check_guess(guess):
    # Step 2: Convert guess to lowercase
    guess = guess.lower()

    # Step 3: Check if the guessed letter is in the secret word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define the ask_for_input function
def ask_for_input():
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Please enter a single letter: ")

        # Step 3: Validate the input
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Step 4: Call check_guess function
    check_guess(guess)

# Step 5: Call ask_for_input to test the functions
ask_for_input()