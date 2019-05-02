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
