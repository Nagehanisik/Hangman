# This is a Hangman Game.
import random

word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Representing each letter with "_" to guess
display = []
word_length = len(chosen_word)
for letter in chosen_word:
    display += "_"
print(display)

# Ask the guess
guess = input("Guess a letter: ").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
