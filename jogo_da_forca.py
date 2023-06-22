import random


def choose_word():
    words = ["banana", "apple", "orange", "pear", "grape"]
    return random.choice(words)


def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(letter if letter in guessed_letters else "_" for letter in word))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly!")
            return

    print(f"Game over! The word was '{word}'. Better luck next time!")


play_game()
