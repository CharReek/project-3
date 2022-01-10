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
    letters_guessed = []
    lives = 6
    print("Let's play a game of Hangman")
    print(hangman_pic(tries))
    print(complete_word)
    print("\n")
    while not guess and tries > 0:
       guessed = input("Please input a word or a letter: ").upper()
       if len(guessed) == 1 and guessed.isalpha():
          if guessed in letters_guessed:
             print("You already gussed that letter, please try again")
       elif len(guessed) == len(word) and guessed.isalpha():
      
       else:
          print("This is not a valid guess, please try again.")
      print(hangman_pic(tries))
      print(complete_word)
      print("\n")



# hangman code taken from a youtube video 
def hangman_pic(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
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