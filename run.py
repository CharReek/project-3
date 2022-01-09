word = "python"

lives = 10
guesses = ["e"]
completed = False

# game play section

while not completed:
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")

print("")
completed = True