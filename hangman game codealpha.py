import random

# Predefined list of words
word_list = ["apple", "house", "train", "phone", "water"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Keep track of guessed letters
guessed_letters = []
correct_letters = ["_"] * len(secret_word)
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(correct_letters))

# Game loop
while incorrect_guesses < max_attempts and "_" in correct_letters:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                correct_letters[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_attempts - incorrect_guesses} guesses left.")

    print("Word:", " ".join(correct_letters))
    print("Guessed letters:", ", ".join(guessed_letters))

# Game result
# if "_" not in correct_letters:
#     print("🎉 Congratulations! You guessed the word:", secret_word)
# else:
#     print("❌ You ran out of guesses. The word was:", secret_word)
#     
# Welcome to Hangman!
# Guess the word: _ _ _ _ _
# Enter a letter: a
# Good guess!
# Word: a _ _ _ _
# Guessed letters: a
# ...

# 
