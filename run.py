import random
from words import words

def select_word():
    word = random.choice(words)
    return word.upper()