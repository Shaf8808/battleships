# Battleships

Battleships is a full back-end Python-based terminal game which runs exclusively in the Code Institute mock terminal on Heroku. 

## How to play

The rules of the game are fairly simple. It begins by asking the user to select a row within the range of 1-9. If the user happens to select a row outside of that range or enter an unrecognised key, they will be given an error message and asked to type in a valid row.

Once a valid row is entered by the user, they are then instructed to enter a column ranging from A to I. This has been programmed in a similar way where if the user enters an invalid column either outside of the range provided or any other key, an error message is displayed and the user is instructed to enter a valid column once more.

After both a valid row and column are entered by the user, a sign is displayed on the board depending on whether or not their guess was correct. If the user managed to successfully "hit" a ship, they are told their guess was correct, and an "X" is displayed on the board which corresponds with the row and column selected by the user. If their guess was incorrect, however, then a "-" is shown on the board, and they are told they guessed incorrectly.

The player has a total of 12 goes to try and sink 10 out of 40 hidden ships on the board. Once they run out of all 12, they are presented with a game-over message and the game ends. If the user successfully manages to guess the correct position of all 10 ships, however, then they are presented with an appropriate congratulatory message and told they have sunk all ships. Upon each successful hit that the user correctly guesses on the board, the turn counter does not decrease to reward the player and to make the game easier for the user to win.

## Table of Contents

* [**Requirements**](#requirements)
* [**Expectations**](#expectations)
* [**Features**](#features)
* [**Data Model**](#data-model)
* [**Technologies Used**](#technologies-used)
    + [Languages](#languages)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Credits**](#credits)

## Requirements

* Ensure the game is responsive to the user as they enter their input
* The game should provide clear and easy-to-understand instructions on the rules and how to play
* User input validation
* A game-over message once the user runs out of turns and fails to hit all the computer's ships
* A game-won message which congratulates the user if they manage to hit all ships successfully

## Expectations

* As a user, I expect the layout of the board game to be organised and easy to understand
* I expect to be provided with clear instructions on how to play the game
* I expect the game to work as intended
* I expect the game to respond to my specific input correctly and appropriately
* I expect to be informed if I have entered an invalid key
* I expect to be informed if I have selected the same row and column as a previous attempt
* I expect the attempt counter to decrease with each attempt
* I expect both my misses and successful hits to be displayed on the board in a way that is easy to identify

[Back to Top](#table-of-contents)

## Features

### Existing Features

* Random board generation
- Generates random ships on the "hidden" board with each attempt
- Includes two boards named player board and hidden board, which store the randomly allocated ships

<img src= "./documentation-images/game-layout.jpg" height=250rem>

* Play against the computer
* Accepts user input
* Input validation and error-checking
- The user is unable to enter an invalid row or column

<img src= "./documentation-images/user-validation.jpg" height=250rem>

- Cannot enter the same coordinates twice

<img src= "./documentation-images/user-validation-two.jpg" height=350rem width=900rem>

- Game over screen

<img src= "./documentation-images/game-over.jpg" height=350rem width=900rem>

- Win game screen

<img src= "./documentation-images/win-game.jpg" height=350rem width=900rem>

[Back to Top](#table-of-contents)

## Data Model

I have decided to use predominantly two boards for my game. One board is the player board which the user sees as they play the game, while the other is a hidden board which only the computer sees and where all of the ships are located.

## Technologies Used

### Languages
* Python

## Testing

During the testing phase of my project, I ran into some issues, such as:

* The structure of each of the functions that my game was going to follow in order. The way I decided to start my project is to lay out all of the main functions that I know my game needed to include before writing the actual logic within each of those functions. I decided this method was the best way to structure my code as it helped me have a clear idea of each function that needed to be implemented for my project to work as intended. I had a few issues structuring my functions as I would sometimes misplace certain functions that needed to execute either after or before another.

I managed to resolve this issue by constantly testing as I wrote each line of code, and printing each line after it was written onto the terminal

* One big issue that had to be looked at was the number of boards that were going to be included in my game. I decided that it would be best to include two, one hidden, and the other a player board that the user would see and interact with during the game. This made it easy for me to structure my code and keep it simple enough for me to make any changes if necessary.

* A big part of my project for making this particular game is user input validation. My game needed to respond appropriately to any form of input from the users' end. It was important, first and foremost, that my game had clear and precise instructions that the user could understand when told to enter a specific input. For example, when I need the user to enter a specific row or column, I displayed the range which the user must keep within when entering their selection, such as 1-9. My code had to include an if statement that would take into consideration each of the scenarios that the game may be presented with based on the players' input. This was the most difficult part of the game, and I am proud that I managed to accomplish this in clear and concise code.

* When it came to user validation, I managed to account for the different types of user input fairly easily, except for one of which I was made aware of by my mentor. When the user pressed the enter key into my input field, my game would move on to the next input before receiving a traceback error in the terminal. This was something I needed to fix for my game and had to spend time identifying which part of my code to specifically target to do so. 

After a while, I realised that it was my get_ship_location function that seemed to be the problem. The method that I had implemented did not account for the user simply pressing the enter key. I resolved this by altering my code and using a try/except method to define the parameters of my user input and include a value error if a suitable number/letter was not entered by the player. This seemed to fix the issue of the user not entering anything before moving on to the next section of the game.

[Back to Top](#table-of-contents)

## Validator Testing

PEP8CI
- No errors were returned

<img src= "./documentation-images/ci-python-linter.jpg" height=350rem>

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
* Clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJs in that order
* Link the Heroku app to the repository
* Click Deploy

## Credits

* Code Institute for the deployment terminal
* [Antonio Rodriguez](https://github.com/AkaAnto)
* [Garrett Broughten](https://github.com/gbrough/battleship/blob/main/single_player.py)


[Back to Top](#table-of-contents)