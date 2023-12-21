from hangman_assets import word_list, stages, logo
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
game_over = False

print(logo)

display = []
for letter in range(word_length):
    display += "_"

print(f"\n{display}")

while not game_over:

    guess = input("Guess: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You loose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Loose")

    if "_" not in display:
        game_over = True
        print("Congratulations,You win!")

    print(stages[lives])
    print(display)
