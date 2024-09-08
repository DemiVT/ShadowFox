import random

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    words = ['python', 'hangman', 'challenge']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess. Attempts left: {max_attempts - incorrect_guesses}")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You've guessed the word.")
            break
    else:
        print(f"Game over. The word was '{word}'.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        hangman()

if __name__ == '__main__':
    hangman()
