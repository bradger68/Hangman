import random

hangman_pics = [
"""
 |-----|
       |
       |
       |
 ______|
""",


"""
 |-----|
 O     |
       |
       |
 ______|
""",


"""
 |-----|
 O     |
 |     |
       |
 ______|""",


"""
 |-----|
 O     |
/|     |
       |
 ______|
 """,


 """
  |-----|
  O     |
 /|\    |
        |
  ______|
  """,


 """
  |-----|
  O     |
 /|\    |
 /      |
  ______|
  """,


"""
 |-----|
 O     |
/|\    |
/ \    |
 ______|
 """
]


# Creates a list of words for the computer to choose from.
words = 'alphabet bear crab drinks entire fringe gild hippo indecisive'.split()

# Makes computer choose a word as the secret word.
def secret_word(word_list):
    wordIndex = random.randint(0, len(word_list) - 1)
    return word_list[wordIndex]

# Records users' valid guesses so far.
guessed_letters = []

# Gets the user to guess a letter.
def get_guess():
    while True:
        guess = input(str(("Guess a letter: ")))
        guess = guess.lower()
        if len(guess) > 1:
            print("Just one letter please.")
        elif guess in guessed_letters:
            print("You already guessed " + guess)
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("A letter please!")
        else:
            guessed_letters.append(guess)
            return guess

# Function that displays the current Hangman situation as well as
# guessed letters and secret word with blanks.

/|     |
       |
 ______|
 """,


 """
  |-----|
  O     |
 /|\    |
        |
  ______|
  """,


 """
  |-----|
  O     |
 /|\    |
 /      |
  ______|
  """,


"""
 |-----|
 O     |
/|\    |
/ \    |
 ______|
 """
]



words = 'alphabet bear crab drinks entire fringe gild hippo indecisive'.split()


def get_guess():
    guess = input(str(("Guess a letter: ")))
    guess = guess.lower()
    if len(guess) > 1:
        print("Just one letter please.")
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("A letter please!")
    else:
        return guess
