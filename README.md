# Coding Hangman
## How to play
My game of hangman is easy to play as it requires only basic input. Users will have to type in a letter each time they would like to guess and then hit enter. The user can also guess the word by typing this out in the input and hitting enter. 

The aim of the game is to guess the word before you run out of lives. Incorrect guesses result in the user losing a life. 

When the user first loads up the game they will see the base hangman structure with stars underneath. Each star represents a letter in the word. As the user guesses these correctly the star will then be replaced by the correct guess. There is 2 outcomes to the game either the user wins or loses. If the user guesses all the letter or the word correctly they will win the game. If not they will lose and they correct word will be shown. 

## Features
### Start Page 
* When the users first goes onto the game it shows as the below.This takes the user straight into the game. From here they can begin to input letters.

insert picture
### Correct Guess 
* When the user makes a correct guess they will be congratulated and then the letter will be added to the stars at the bottom in the correct place. The congratulations message shows up in green so it stands out from the rest of the text. 

![StartPage] (assests/images/hangman 1.PNG)

### Incorrect Guess 
*  When the user makes an incorrect guess a life is deducted and a part of the hangman picture is added. 

![IncorrectGuess] (assests/images/hangman9.PNG)

### Repeat letter 
* If the user guesses a letter twice then a message will come up asking them to try again and input another letter. 

![RepeatLetter] (assests/images/hangman10.PNG)

### Lives Remaining
* The lives remaining feature shows the user how many attempts they have left. 

![Lives] (assests/images/hangman3.PNG)

### Letters Guessed 
* The letters guessed shows what letters the user has already guessed so they are aware of what letters have been ruled out. 

![LettersGuessed] (assests/images/hangman4.PNG)

### Play Again 
* The play again feature gives the user to play the game again, They have 2 answers Yes or No, if they chose yes the game restarts if they say no they get a message that says thank you for playing 

![PlayAgain] (assests/images/hangman8.PNG) 

## Technologies
* Python was the language of choice to program this game. 
* Github was used to store all the code.
* Gitpod was used to write the code and commit and push my changed to the repository. 
* Heroku was used to deploy the game.

## Testing 
### Validator testing 
* No errors were found when the code was passed through the PEP8 linter
![pep8Test] (assests/images/pep8.PNG)

 ### Manual Testing 
1. Testing correct letter 
   * In order to make sure that the correct letter showed up when enter i tested this by doing the below: 
      * To make sure I guessed the correct letters i tested this before adding in the random function, this way i could ensure that i was guessing the correct letters. I Guessed each of the correct letter to ensure that it replaced the * and the Well Done message came up.
2. Testing incorrect letter 
   * To test that the incorrect letter returned the right output i tested this by playing the game and using different letters. 
     * I inputted random letters to see if they were in the word and the correct message came up. I did this by using more obscure letters such a "Z". I then added in correct letter to make sure that the incorrect function worked each time. I also made sure that the letters added into the letter guessed list.
3. Testing Number or symbol input 
   * In order to make sure that a number or symbol could not be inputted i tested this by trialing it. 
      * I tested this by playing the game and inputting both numbers and symbols to make sure the correct message came up. The message that came up when a number or Symbol was inputted is "This is not a valid guess. Please try again". I also checked that it did not deduct a life from the lives.
4. Testing Correct word guees 
  *  Giving the ability to the user to guess the correct work i had to test this function. 
     * I did this by guessing a few letters and then checking in my list of words to see what i could be. I then inputted the correct word to ensure that it showed the correct message showed up. I also tested that it then called the restart game function. 
5. Testing incorrect word guess
   * Giving the ability to the user to guess the correct work i had to test this function. 
      *  I did this by guessing a random word that i knew was not in my list to make sure that it showed the correct message and took the user back to guessing a letter. 
6. Testing running out of lives
   * Due to having a life counter i needed to test that these depreciated when the guess was incorrect and that the correct part of the hangman was added each time. 
      * To do this i tested both getting a letter correct and incorrect to make sure that a life was taken away and a part of the hangman picture was added on. I tested this mutiple times until the hangman picture was completed 
7. Testing play again - Yes
   * The addition of the play again feature at the end of the game, gives the user the option to either replay the game or exit the function. 
     * To test this i inputted both correct and incorrect letters untill i ran out of lives. When the restart question came up i enter "Y", This then restarted the game.
8. Testing play again - No 
   * The addition of the play again feature at the end of the game, gives the user the option to either replay the game or exit the function. 
     * To test this i inputted both correct and incorrect letters untill i ran out of lives. When the restart question came up i enter "N". This then brings up the message "Thank you for playing Hangman"

### Bugs 
* As stated above i have manual tested all outcomes of my game to ensure there were no bugs. 

## Deployment 
The below steps show how i deployed my game to heroku
1. Go to the Heroku website and log in
2. Click New in the top right corner, from the drop down select create new app
3. Chose a name for your app, once you have done this, click create app
4. Go to the Settings tab and scroll down to Config Vars
5. Add a new Config Var, input the key word as PORT and value as 8000
6. After this go to the Deploy tab
7. Once you are on the deploy tab scroll down and set the deployment method GitHub. 
8. Once this has been connected, find your repository
9. When you ahve conected this scroll down to manual Deployment 
10. Ensure the MAIN branch is selected and then click Deploy Branch

My deployed game can be found via the below link:
https://project-3-hangman.herokuapp.com/ 

## Credits
* The code for the hangman imagery was taken from - https://www.youtube.com/watch?v=m4nEnsavl6w&t=160s
* I used mutiple youtube vidoes to help me understand the concpet of hangman with python 
* I Used stack overflow to help me add the colour into the terminal 
* The terminal used to host the game was created by Code Institue 
* I Used the Code Institue deployment lesson to help me deploy my site
