# Battleships

Battleships is a fully back-end Python based terminal game which runs exclusively in the Code Institute mock terminal on Heroku. 

## How to play

The rules of the game are fairly simple. It begins by asking the user to select a row within the range of 1-9. If the user happens to select a row outside of that range, or enter a key which is unrecognised, they will be given an error message and asked to type in a valid row.

Once a valid row is entered by the user, they are then instructed to enter a column rangiing from A to I. This has been programmed in a similar way where if the user enters an invalid column either outside of the range provided or any other key, an error message is displayed and the user is instructed to anter a valid column once more.

After both a valid row and column is entered by the user, a sign is displayed on the board depending on whether or not their guess was correct. If the user managed to successfully "hit" a ship, they are told their guess was correct, and an "X" is displayed on the board which corresponds with the row and column selected by the user. If their guess was incorrect, however, then a "-" is shown on the board, and they are told they missed.

The player has a total of 10 goes to try and sink all 5 of the hidden ships on the board. Once they run out of all 10, they are presented with a game over message and thr game ends. If the user successfully manages to guess the correct position of all 5 ships, however, then they are presented with an appropriate congratulatory message and told they have sunk all ships.

## Features

### Existing Features

* Random board generation
- Generates random ships on the "hidden" board with each attempt
- Includes two boards named player board and hidden board, which stores the randomly allocated ships

<img src= "./documentation-images/game-layout.jpg">

* Play against the computer
* Accepts user input
* Input validation and error-checking
- The user is unable to enter an invalid row or column

<img src= "./documentation-images/user-validation.jpg">

- Cannot enter the same coordinates twice

## Data Model

I have decided to use a constant board class using predominantly two boards. One board is the player board which the user sees as they play the game, while the other is a hidden board which only the computer sees and where all of the ships are located.

## Testing

During the testing phase of my project, I ran into some issues, such as:

* Correctly structuring each of the functions that my game was going to follow in order. The way I decided to start my project is to layout all of the main functions that I know my game needed to include before writing the actual logic within each of those functions. I decided this method was the best way to structure my code as it helped me have a clear idea of each function that needed to be implemented for my project to work as intended. I had a few issues structuring my functions as I would sometimes misplace certain functions that needed to execute either after or before another.

I managed to resolve this issue by constantly testing as I wrote each line of code, and printing each line after it was written onto the terminal

* One big issue that had to be looked at was the number of boards that was going to be included in my game. I decided that it would be best to include two, one hidden, and the other a player board that the user would see and interact with during the game.

## Validator Testing

PEP8
- No errors were returned

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the builbacks to Python and NodeJs in that order
* Link the Heroku app to the repository
* CLick Deploy

## Credits

* Code Institute for the deployment terminal
* Garrett Broughten


