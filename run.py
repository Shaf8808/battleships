# Legend
# X for placing ship and hit battleship
# ' ' for empty space
# '-' for missed shot

from random import random


HIDDEN_BOARD = [[' '] * 10 for x in range(10)]
GUESS_BOARD = [[' '] * 10 for x in range(10)]


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}


def print_board(board):
    print('     A B C D E F G H')
    print('     ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(7):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row]


def get_ship_location():
    pass


def count_hit_ships():
    pass


create_ships()
turns = 10
# while turns > 0:
