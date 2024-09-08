import random

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    words = ['python', 'hangman', 'challenge']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

        current_display = display_word(word, guessed_letters)
        print(current_display)
        
        if '_' not in current_display:
            print("Congratulations! You've guessed the word.")
            break
    else:
        print(f"Game over. The word was '{word}'.")

if __name__ == '__main__':
    hangman()
