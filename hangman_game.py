import random

WORDS = ['apple', 'banana', 'cherry']
chosen_word = random.choice(WORDS)
print(chosen_word)
available_lives = 4
current_word = []
for _ in range(len(chosen_word)):
    current_word += '_'

no_blank_spaces = len(current_word)
print('Welcome to Hangman. You have 4 lives available')

while no_blank_spaces:
    user_choice = input("Guess a letter: ").lower()

    letter_matched = False
    for position in range(len(chosen_word)):
        if user_choice == chosen_word[position]:
            letter_matched = True
            no_blank_spaces -= 1
            current_word[position] = user_choice
            print(current_word)

    if not letter_matched:
        available_lives -= 1
        print(f"You have {available_lives} lives left.")

    if available_lives == 0:
        print("You lost!")
        break
