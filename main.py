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

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
