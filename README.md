# Hangman
## How to play
My game of hangman is easy to play as it requires only basic input. Users will have to type in a letter each time they would like to guess and then hit enter. The user can also guess the word by typing this out in the input and hitting enter. 
The aim of the game is to guess the word before you run out of lives. Incorrect guesses result in the user losing a life. 
When the user first loads up the game they will see the base hangman structure with stars underneath. Each star represents a letter in the word. As the user guesses these correctly the star will then be replaced by the correct guess. There is 2 outcomes to the game either the user wins or loses. If the user guesses all the letter or the word correctly they will win the game. If not they will lose and they correct word will be shown. 

## Features

## Technologies
* Python was the language of choice to program this game. 
* Github was used to store all the code.
* Gitpod was used to write the code and commit and push my changed to the repository. 
* Heroku was used to deploy the game.

## Testing 
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
5. Testing incorrect word guess 
6. Testing all correct guesses 
7. Testing rnning out of lives
8. Testing play again - Yes
9. Testing play again - No 

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
