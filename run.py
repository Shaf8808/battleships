from random import randint

# Board for holding computer ship locations
HIDDEN_BOARD = [[' '] * 9 for x in range(9)]
# Board that the user sees and displays their hits and misses
PLAYER_BOARD = [[' '] * 9 for y in range(9)]

# Used during user input and displaying player board with the
# correct rows and columns structured in order
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8
}


def print_board(board):
    """
    The structure and layout of the board
    which is presented to the user once they
    begin the game
    """
    print('  A B C D E F G H I')
    print('  -+-+-+-+-+-+-+-+-+')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print('  -+-+-+-+-+-+-+-+-+\n')


def create_ships(board):
    """
    Function for creating a maximum of
    5 ships for the user to try and hit
    """
    for ship in range(40):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Function for user input creating it's
    parameters and displaying an error message
    if the user enters an invalid key
    """
    while True:
        try:
            row = input('Please enter a ship row 1-9: ')
            if row in "123456789":
                row = int(row) - 1
                break
        except ValueError:
            print('Please enter a valid number between 1-9: ')
    while True:
        try:
            column = input('Please enter a ship column A-I: ').upper()
            if column in 'ABCDEFGHI':
                column = letters_to_numbers[column]
                break
        except KeyError:
            print('Please enter a valid column between A-I')
    return row, column


def count_hit_ships(board):
    """
    Checks if all of the ships have been
    successfully hit by the user
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 15
# Loop that runs continuously until either the user runs out of turns
# or if they successfully hit all ships
while turns > 0:
    print('\nWelcome to Battleship, where you have a total of 15 turns to try '
          'and sink 40 hidden ships on the computers board. Upon a '
          'successful hit, your turn counter will not go down. '
          'Good luck and choose wisely...\n')
    print("Legend: X for hit battleship \n        - for missed shot\n")
    print_board(PLAYER_BOARD)
    row, column = get_ship_location()
    if PLAYER_BOARD[row][column] == '-':
        print('Row and column already selected')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Successful hit!')
        PLAYER_BOARD[row][column] = 'X'
    else:
        print('\nTough luck friend, you missed!')
        PLAYER_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(PLAYER_BOARD) == 5:
        print('Congratulations! You have sunk all of those pesky ships!')
        break
    print(f'You have {str(turns)} turns remaining')
    if turns == 0:
        print('Game Over!')
        break
