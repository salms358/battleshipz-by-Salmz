#  Battleships By Salmz

## Introduction 

Welcome to my Battleships game. Its a very basic variation of the classic Battleships game. 
The aim of the game is to sink of the computers ships.

A live version of the game can be found here []


# Strategy 
## Flowchart

![flowchart p1](https://user-images.githubusercontent.com/119611403/234128111-f7f46457-baf0-4a46-acec-164398898efa.jpg)

![flowchart p2](https://user-images.githubusercontent.com/119611403/234128860-c305a7f6-f845-43e7-af58-a727ae99f915.jpg)

                       END
## Project Goals
The main aim of the game is to have fun whilst improving the users strategy skills. In this game the user will play against a computer.

## User Goals
First time players:
- I want to be told the rules if i am not sure of how to play.
- I want the game to be engaging. Im going to see if i can beat the computer first time.
- I want the game to be easy to navigate around.

Frequent time user:
- I enjoy playing the game but sometimes i wish the columns were not so squished together.

# Structure
## The flow of the game:
![hompage](https://user-images.githubusercontent.com/119611403/233997780-c85e7363-1075-4731-b09c-ac18a63152a3.png)

Firstly the user is presented with the hompage which shows ASCII art of a ship and a welcome message to help the users feel comfortable and happy.

![the rules](https://user-images.githubusercontent.com/119611403/233999324-eac13231-640c-4991-8a46-e98967f31b99.png)


Right after the user is welcomed they are asked if they want to see the rules of the game just incase they are not familiar with the rules. A "Lets gooo" message is displayed to indicate that the game is starting.

![difficulties](https://user-images.githubusercontent.com/119611403/234001742-cdddfd95-e6f9-4817-9f5c-544f505b7f96.png)

The difficulty levels are then displayed prompting the user to choose if they want to play on easy, medium or hard mode by selecting the number 1, 2, or 3.
Once the diffuculty level has been chosen the boards will display and depending on the diffulty level the user chose the board would either be 7 x 7, 10 x 10 or 12 x 12. As the bigger the board gets it will be harder to hit the 5 ships on the board.

![easy mode](https://user-images.githubusercontent.com/119611403/234003676-5f3e01e4-b99e-419c-bbce-6480c2b14335.png)

if the user chooses the easy mode this is the grid they will be presented with.

![medium mode](https://user-images.githubusercontent.com/119611403/234003975-862f3740-6a17-4619-a575-7242d1bd0813.png)

if the user chooses the medium mode this is the grid they will be presented with.

![hard mode ](https://user-images.githubusercontent.com/119611403/234004278-4fc62cac-d21a-4d40-a65c-14f3233f5021.png)

if the user chooses the hard mode this is the grid they will be presented with.


# How to play
Battleship is a 2 player game and involves playing against a computer. The user should enter in a value between 0-7 if they chose the easy mode, 0-10 if they choose the medium mode and 0-12 if they choose the hard modes. If the user enter in too many incorrect guesses the game will end. Moreover if the user sinks all the battleships the user will win the game. Once the user guesses their row and column the computer will respond with their guess and it should state if the hit or miss their guess.

# Features
- 5 ships present per game for both user and computer
- user ships marked with S whereas ships are concealed on the computer board they are revealed once they have been hit.
- Ships are randomly generated onto both user and computer boards. 
- first to hit all ships wins 


# Testing
- To test i purposely entered in incorrect values so i can get error messages from the programme to be printed out.
- I put the code into pep8 validator then corrected errors from there. When re doing the pep 8 validator it got 68% with most of the problems to do with white spaces. The pep8 also said it was around 68% correct due to these white space problems.

![errors](https://user-images.githubusercontent.com/119611403/234338163-6f3b5a4d-8c89-48fd-9be6-8e685819cf0e.jpg)


- Print statements were used across the programme to make sure the code was running as it should be. Then these placeholder print statements were removed.


## Solved bugs
- Initially the ships on the computer board were not concealing which defeats the purpose of the game the code was present but not working so this code had to be removed and a third bored had to be added to replace the computer board when the player hit or miss. 
- The grid size starts from 0 to 7 with the easy mode it always picks up the user input as one more than it is e.g 3,1 is 4,2
- The computer always misses which i am concerned about im not sure why this was happening.
## Unsolved bugs 
- The computers grid involves starting from 0 as when the computer makes a guess it will be one more than it is just like how the empty_board was previously
- When the user guesses the same coordinate it will state that they have entered in the same coordinate but the number of guesses will still decrease. 

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