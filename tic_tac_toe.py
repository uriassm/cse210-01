#CSE 210 Week 02 Tic-Tac-Toe assignment.
#Author: Urias Miranda

def main():
    game_start = 'y'
    while game_start == 'y':
        spaces_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        make_board(spaces_list)
        print()

        while not (winner(spaces_list) or draw(spaces_list)):
            x_turn = int(input("x's turn to choose a square (1-9): "))
            spaces_list[x_turn - 1] = 'x'

            print()
            make_board(spaces_list)
            print()

            if winner(spaces_list) or draw(spaces_list):
                break

            o_turn = int(input("o's turn to choose a square (1-9): "))
            spaces_list[o_turn -1] = 'o'

            print()
            make_board(spaces_list)
            print()
        game_start = input('Would you like to play again? (y/n): ')
    print()
    print('Thank you for playing!')

def make_board(spaces):
    row_divider = '-+-+-'

    print(f'{spaces[0]}|{spaces[1]}|{spaces[2]}')
    print(row_divider)
    print(f'{spaces[3]}|{spaces[4]}|{spaces[5]}')
    print(row_divider)
    print(f'{spaces[6]}|{spaces[7]}|{spaces[8]}')

def winner(spaces):
    if spaces[0] == spaces[1] == spaces[2]:
        print(f'{spaces[0]} won this round!')
        return True
    elif spaces[3] == spaces[4] == spaces[5]:
        print(f'{spaces[3]} won this round!')
        return True
    elif spaces[6] == spaces[7] == spaces[8]:
        print(f'{spaces[6]} won this round!')
        return True
    elif spaces[0] == spaces[3] == spaces[6]:
        print(f'{spaces[0]} won this round!')
        return True
    elif spaces[1] == spaces[4] == spaces[7]:
        print(f'{spaces[1]} won this round!')
        return True
    elif spaces[2] == spaces[5] == spaces[8]:
        print(f'{spaces[2]} won this round!')
        return True
    elif spaces[0] == spaces[4] == spaces[8]:
        print(f'{spaces[0]} won this round!')
        return True
    elif spaces[2] == spaces[4] == spaces[6]:
        print(f'{spaces[2]} won this round!')
        return True

def draw(spaces):
    for i in range(9):
        if spaces[i] != 'x' and spaces[i] != 'o':
            return False
        
    print('The game is a draw.')
    return True

if __name__ == '__main__':
    main()