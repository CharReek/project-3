import random

from words import words

# select word function


def select_word():
    """
    select word functiom
    """
    word = random.choice(words)
    return word.upper()

# game play function


def game_play(word):
    """
    game play function
    """
    complete_word = "_" * len(word)
    guess = False
    words_guessed = []
    letters_guessed = []
    tries = 6
    print("Let's play a game of Hangman")
    print(hangman_pic(tries))
    print(complete_word)
    print("\n")
    while not guess and tries > 0:
        guessed = input("Please input a word or a letter: ").upper()
        if len(guessed) == 1 and guessed.isalpha():
            if guessed in letters_guessed:
                print("You already gussed that letter, please try again")
            elif guessed not in word:
                print(f"{guessed} is not in the word")
                tries -= 1
                letters_guessed.append(guessed)
            else:
                print("well done you guessed correctly!")
                letters_guessed.append(guessed)
                list_of_words = list(complete_word)  # turns a string to a list
                # finds where guessed occurs in the word
                indicies = [i for i, letter in enumerate(
                    word) if letter == guessed]

                # replaces the underscore with the guessed letter
                for index in indicies:
                    list_of_words[index] = guessed
                complete_word = "".join(list_of_words)
                if "_" not in complete_word:
                    guess = True

        # conditional for guessing a word
        elif len(guessed) == len(word) and guessed.isalpha():
            if guessed in words_guessed:
                print("you have already guessed this word")
            elif guessed != word:
                print("That guess is incorrect, Please try again")
                tries -= 1
                words_guessed.append(guessed)
            else:
                guessed = True
                complete_word = word
        else:
            print("This is not a valid guess, please try again.")
        print(hangman_pic(tries))
        print(complete_word)
        print("\n")
    if guess:
        print("Well done you guessed the word correctly!")
    else:
        print("Looks like you ran out of lives, Better luck next time")

# hangman code taken from a youtube video


def hangman_pic(tries):

    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def start():
    word = select_word()
    game_play(word)


start()
