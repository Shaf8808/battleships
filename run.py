# Legend
# X for placing ship and hit battleship
# ' ' for empty space
# '-' for missed shot

from random import randint


HIDDEN_BOARD = [[' '] * 9 for x in range(9)]
PLAYER_BOARD = [[' '] * 9 for x in range(9)]


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
    print('  A B C D E F G H I')
    print('  ------------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 8), randint(0, 8)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 8), randint(0, 8)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    row = input('Please enter a ship row 1-9')
    while row not in '123456789':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-9')
    column = input('Please enter a ship column A-I').upper()
    while column not in 'ABCDEFGHI':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-I').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to the best Battleship game in the WORLD!')
    print_board(PLAYER_BOARD)
    row, column = get_ship_location()
    if PLAYER_BOARD[row][column] == '-':
        print('Row and column already selected')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('Successful hit!')
        PLAYER_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('Tough luck friend, you missed!')
        PLAYER_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(PLAYER_BOARD) == 5:
        print('Congratulations! You have sunk all of those pesky ships and have earned the title master of the seas!')
        break
