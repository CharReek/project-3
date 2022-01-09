import random

words = ["python", "computer", "java", "internet", "website"]


def get_word():
    """
    selects a random word from the list of words
    """
    return (random.choice(words)).upper()


def play_game():
    """
    hangman game function
    """
    word = get_word()
    word_letters 

    lives = 10