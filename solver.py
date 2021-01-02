import pprint
import random

pp = pprint.PrettyPrinter()

board = [
	[0, 0, 0, 9, 0, 6, 0, 0, 0],
	[4, 2, 0, 0, 0, 8, 6, 0, 0],
	[0, 0, 1, 0, 0, 7, 2, 0, 8],
	[8, 0, 0, 4, 0, 9, 5, 1, 7],
	[7, 4, 0, 0, 0, 1, 9, 3, 0],
	[0, 9, 6, 7, 3, 0, 0, 2, 0],
	[0, 0, 0, 5, 1, 3, 0, 6, 0],
	[2, 0, 7, 6, 0, 4, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 4, 5, 9],
]

boxes_on_board = {
    (0, 0): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    (0, 1): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
    (0, 2): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
    (1, 0): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
    (1, 1): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
    (1, 2): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
    (2, 0): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
    (2, 1): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
    (2, 2): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
}

# Return to this and implement backtracking for higher level puzzles
def solve(board):
    if is_board_complete(board):
        print("This is the final board:")
        pp.pprint(board)
        return board
    
    empty_positions = get_empty_positions_with_possible_guesses(board)
    for position_dict in empty_positions:
        for key in position_dict:
            if len(position_dict[key]) == 1:
                add_number(board, key, position_dict[key][0])
                empty_positions.remove(position_dict)

    pp.pprint(board)
    solve(board)

def get_empty_spaces(board):
    empty_spaces_array = []
    for row_index, row in enumerate(board):
        for space_index, space in enumerate(row):
            if space == 0:
                empty_spaces_array.append((row_index, space_index))

    return empty_spaces_array

def get_boxes_of_empty_spaces(empty_spaces_array):
    get_empty_spaces(board)

def add_number(board, position, number):
    board[position[0]][position[1]] = number

def get_tryable_numbers(board, position):
    # All possible numbers
    tryable_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Possible numbers after removing numbers already found in row
    for number in board[position[0]]:
        if number in tryable_numbers:
            # print(number)
            tryable_numbers.remove(number)

    # Possible numbers after removing numbers already found in column
    for row in board:
        if row[position[1]] in tryable_numbers:
            tryable_numbers.remove(row[position[1]])

    # Possible numbers after removing numbers already found in 3x3 box
    box_of_position = (position[0]//3, position[1]//3)
    for coord in boxes_on_board[box_of_position]:
        if board[coord[0]][coord[1]] in tryable_numbers:
            tryable_numbers.remove(board[coord[0]][coord[1]])

    return tryable_numbers

def get_empty_positions_with_possible_guesses(board):
    empty_spaces_array = get_empty_spaces(board)
    empty_positions_with_possible_guesses = []

    for empty_space_coord in empty_spaces_array:
        possible_numbers_array = get_tryable_numbers(board, empty_space_coord)
        empty_positions_with_possible_guesses.append({empty_space_coord: possible_numbers_array})
    
    return empty_positions_with_possible_guesses

def is_board_complete(board):
    for row in board:
        for space in row:
            if space == 0:
                return False
    
    return True

solve(board)