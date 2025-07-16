import random

def hangman():
    words = ["apple", "python", "banana", "orange", "grapes"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    display = ["_" for _ in word]

    while attempts > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if "_" not in display:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

hangman()