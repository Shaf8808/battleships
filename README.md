# Battleships

Battleships is a fully back-end Python based terminal game which runs exclusively in the Code Institute mock terminal on Heroku. 

## How to play

The rules of the game are fairly simple. It begins by asking the user to select a row within the range of 1-9. If the user happens to select a row outside of that range, or enter a key which is unrecognised, they will be given an error message and asked to type in a valid row.

Once a valid row is entered by the user, they are then instructed to enter a column rangiing from A to I. This has been programmed in a similar way where if the user enters an invalid column either outside of the range provided or any other key, an error message is displayed and the user is instructed to anter a valid column once more.

After both a valid row and column is entered by the user, a sign is displayed on the board depending on whether or not their guess was correct. If the user managed to successfully "hit" a ship, they are told their guess was correct, and an "X" is displayed on the board which corresponds with the row and column selected by the user.


