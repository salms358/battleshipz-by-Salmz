#  Battleships By Salmz

## Introduction 

Welcome to my Battleships game. Its a very basic variation of the classic Battleships game. 
The aim of the game is to sink of the computers ships.

A live version of the game can be found here []

# Strategy 
## Project Goals
The main aim of the game is to have fun whilst improving the users strategy skills.In this game the user will play against a computer.

## User Goals
First time players:
- I want to be told the rules if i am not sure of how to play.
- I want the game to be engaging.Im going to see if i can beat the computer first time.
- I want the game to be easy to navigate around.

Frequent time user:
- I enjoy playing the game but sometimes i wish the columns were not so squished together.

# Structure

# How to play
Battleship is a 2 player game and involves playing against a computer. The user should enter in a value between 0-7 if they chose the easy mode, 0-10 if they choose the medium mode and 0-12 if they choose the hard modes. If the user enter in too many incorrect guesses the game will end. Moreover if the user sinks all the battleships the user will win the game. Once the user guesses their row and column the computer will respond with their guess and it should state if the hit or miss their guess.

# Features
- 5 ships present per game for both user and computer
- user ships marked with S whereas ships are concealed on the computer board they are revealed once they have been hit.
- Ships are randomly generated onto both user and computer boards. 
- first to hit all ships wins 

The screenshot below shows my ASCII Art design to make user feel more welcome before they start playing the battleships game
(https://github.com/salms358/battleshipz-by-Salmz/blob/main/intro%20to%20game.jpg)

This shows if the user chooses to view the rules of the game before they start just incase they want a refresher of the rules.
(https://github.com/salms358/battleshipz-by-Salmz/blob/main/rules%20feature.jpg)

Thes status is shown on top of the board each time the user and computer have goes 
(https://github.com/salms358/battleshipz-by-Salmz/blob/main/status.jpg)

# Testing
- To test i purposely entered in incorrect values so i can get error messages from the programme to be printed out.
- I put the code into pep8 validator then corrected errors from there. When re doing the pep 8 validator it got 68% with most of the problems to do with white spaces.
here is a link to the validator score:
(https://github.com/salms358/battleshipz-by-Salmz/blob/main/validatorz.jpg)

- Print statements were used across the programme to make sure the code was running as it should be. Then these placeholder print statements were removed.


## Solved bugs
- Initially the ships on the computer board were not concealing which defeats the purpose of the game the code was present but not working so this code had to be removed and a third bored had to be added to replace the computer board when the player hit or miss. 

## Unsolved bugs 
- The grid size starts from 0 to 7 with the easy mode it always picks up the user input as one more than it is e.g 3,1 is 4,2
- The computer always misses which i am concerned about im not sure why this was happening.
- Sometimes the computer picks the same coordinates as before.
- There is a problem with 

# Deployment
1. I used Heroku to deploy my final project to the cloud. To do this I had to:
2. Push all latest code to GitHub.
3. Go to Heroku
4. Select new in the top right corner.
5. Create new app.
6. Enter the app name and select Europe as the region.
7. Connect to GitHub.
8. Search for repo-name.
9. Select connect to the relevant repo you want to deploy.
10. Select the settings tab.
11. Add buildpack
12. Select Python, then save changes.
13. Select Nodejs, then save changes.
14. Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
15. Navigate to the deploy tab
16. Scroll down to Manual Deploy and select deploy branch.

# Credits
https://github.com/iKelvvv/MS3 Helped me with source code.

Marcel Mentor

You tube tutorial to come up with basic structure for code (https://www.youtube.com/watch?v=tF1WRCrd_HQ)
I got the ASCII art of ship from here (https://ascii.co.uk/art/ships)

w3 schools taught me about randint as ive never learnt about it before