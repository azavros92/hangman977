import random  # Step 2: Import the random module

# Step 1: Create a list of your 5 favorite fruits
word_list = ["Mango", "Strawberry", "Blueberry", "Pineapple", "Watermelon"]

# Step 3 & 4: Use random.choice to pick a word and assign it to 'word'
word = random.choice(word_list)

# Step 5: Print the randomly selected word
print(word)

# Step 1: Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Step 2: Assign the input to a variable called guess
print(f"You entered: {guess}")

# Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!"
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met
    print("Oops! That is not a valid input.")