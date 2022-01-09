import random

words = ["python", "computer", "java", "internet", "website"]


def get_word():
    """
    selects a random word from the list of words
    """
    return (random.choice(words)).lower()