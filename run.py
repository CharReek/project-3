"""
imports the random function, use to shuffle words
"""
import random


from words import words


class Colors:
    """
    colours for the text
    """
    RED = '\033[91m'
    GREEN = '\033[92m'
    WHITE = '\033[0m'
    BLUE = '\33[104m'


def select_word():
    """
    select word functiom
    """
    word = random.choice(words)
    return word.upper()


def game_play(word):
    """
    game play function
    """
    complete_word = "*" * len(word)
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
                print(Colors.RED + "You already gussed that letter,Try again"
                      + Colors.WHITE)
            elif guessed not in word:
                print(f"{guessed} is not in the word")
                tries -= 1
                letters_guessed.append(guessed)
            else:
                print(Colors.GREEN + "well done you guessed correctly!"
                      + Colors.WHITE)
                letters_guessed.append(guessed)
                list_of_words = list(complete_word)  # turns a string to a list
                # finds where guessed occurs in the word
                indicies = [i for i, letter in enumerate(
                    word) if letter == guessed]

                # replaces the underscore with the guessed letter
                for index in indicies:
                    list_of_words[index] = guessed
                complete_word = "".join(list_of_words)
                if "*" not in complete_word:
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
            print(Colors.RED + "This is not a valid guess, please try again."
                  + Colors.WHITE)
        print(hangman_pic(tries))
        print(f"{Colors.BLUE}Lives remaining:{tries}{Colors.WHITE}\n")
        print("Letters Guessed:" + ",". join(sorted(letters_guessed)) + "\n")
        print(complete_word)
        print("\n")
    if guess:
        print(Colors.GREEN + "Well done you guessed the word correctly!"
              + Colors.WHITE)
        play_again()
    else:
        print(f"{Colors.RED} Looks like you ran out of lives"
              f" The correct word was:{Colors.WHITE} {word}")
        print("\n")
        play_again()
# hangman code taken from a youtube video


def play_again():
    """
    function that asked if the person
    wants to play the game again
    """
    restart = False

    while not restart:
        again = input("Would you like to play again? (Y/N)")
        try:
            if again == "Y":
                restart = True
                start()
            elif again == "N":
                restart = True
                print("Thank you for playing Hangman")
            else:
                raise ValueError("Please enter Y or N")

        except ValueError:
            print("Please try again")


def hangman_pic(tries):
    """
    code for hangman pictures
    this was taken from a youtube video
    """

    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
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
    """
    sets up the game ready to play
    """
    word = select_word()
    game_play(word)


start()
