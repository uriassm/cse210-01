#CSE 210 Week 02 Tic-Tac-Toe assignment.
#Author: Urias Miranda

def main():
    try:
        game_start = 'y'
        while game_start != 'n':
            game_spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            selected_space = 0
            horizontal_grid_spaces = 3
            vertical_grid_spaces = 3

            game_board()
            game_start = 'n'
    except ValueError as val_err:
        'incorrect'

def game_board():
    '''Creates the gameboard with correct #x# grid'''
    first_row = ['1', '|', '2', '|', '3']
    second_row = ['4', '|', '5', '|', '6']
    third_row = ['7', '|', '8', '|', '9']
    row_divider = '-+-+-'

    print(''.join(first_row))
    print(row_divider)
    print(''.join(second_row))
    print(row_divider)
    print(''.join(third_row))

if __name__ == '__main__':
    main()