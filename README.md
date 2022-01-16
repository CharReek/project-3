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
