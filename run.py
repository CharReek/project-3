import random
from words import words
 
# select word function

def select_word():
    word = random.choice(words)
    return word.upper()

# game play function 

def game_play(word):
    complete_word = "_" * len(word)
    guess = False
    words_guessed = []
    letters_guesses = []