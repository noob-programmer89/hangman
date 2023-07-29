# Hangman Game

import random
from hangman_art import logo, stages
from hangman_words import word_list

# Number of lives the player has
lives = 6

# Variable to keep track of the game status
end_of_game = False

# Choose a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# List to store the current state of the word being guessed
word_list = ["_" for _ in range(word_length)]

# Display the game logo
print(logo)

# Game loop
while not end_of_game:
    # Ask the player to make a guess
    guess = input("\nGuess a letter: ").lower()

    # Check if the guess is already made
    if guess in word_list:
        print(f"You have already guessed the letter: {guess}")
    else:
        # Check if the guess is in the chosen word
        for pos in range(word_length):
            if chosen_word[pos] == guess:
                word_list[pos] = guess

        # Display the current state of the word
        print(f"{' '.join(word_list)}")

        # Check if all letters have been guessed correctly
        if "_" not in word_list:
            end_of_game = True
            print("Congratulations! You guessed the word.")

        # Check if the guess is not in the chosen word
        if guess not in chosen_word:            
            lives -= 1
            print(f"Wrong guess! You have {lives} attempts left.")
            print(stages[lives])
            
            # Check if the player has run out of lives
            if lives == 0:
                end_of_game = True
                print(f"You lose! The word was {chosen_word}")

        