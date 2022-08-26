#!/usr/bin/env python3
from itertools import count
from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
history = []

def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    win_state = [
        #Hàng Ngang
        [state[0][0], state[0][1], state[0][2], state[0][3], state[0][4]],
        [state[0][1], state[0][2], state[0][3], state[0][4], state[0][5]], 
        [state[1][0], state[1][1], state[1][2], state[1][3], state[1][4]],
        [state[1][1], state[1][2], state[1][3], state[1][4], state[1][5]],
        [state[2][0], state[2][1], state[2][2], state[2][3], state[2][4]],
        [state[2][1], state[2][2], state[2][3], state[2][4], state[2][5]],
        [state[3][0], state[3][1], state[3][2], state[3][3], state[3][4]],
        [state[3][1], state[3][2], state[3][3], state[3][4], state[3][5]],
        [state[4][0], state[4][1], state[4][2], state[4][3], state[4][4]],
        [state[4][1], state[4][2], state[4][3], state[4][4], state[4][5]],
        [state[5][0], state[5][1], state[5][2], state[5][3], state[5][4]],
        [state[5][1], state[5][2], state[5][3], state[5][4], state[5][5]],
        #Hàng Dọc
        [state[0][0], state[1][0], state[2][0], state[3][0], state[4][0]],
        [state[1][0], state[2][0], state[3][0], state[4][0], state[5][0]],
        [state[0][1], state[1][1], state[2][1], state[3][1], state[4][1]],
        [state[1][1], state[2][1], state[3][1], state[4][1], state[5][1]],
        [state[0][2], state[1][2], state[2][2], state[3][2], state[4][2]],
        [state[1][2], state[2][2], state[3][2], state[4][2], state[5][2]],
        [state[0][3], state[1][3], state[2][3], state[3][3], state[4][3]],
        [state[1][3], state[2][3], state[3][3], state[4][3], state[5][3]],
        [state[0][4], state[1][4], state[2][4], state[3][4], state[4][4]],
        [state[1][4], state[2][4], state[3][4], state[4][4], state[5][4]],
        [state[0][5], state[1][5], state[2][5], state[3][5], state[4][5]],
        [state[1][5], state[2][5], state[3][5], state[4][5], state[5][5]],
        # Hàng Chéo Bên Trái
        [state[5][0], state[4][1], state[3][2], state[2][3], state[1][4]],
        [state[4][1], state[3][2], state[2][3], state[1][4], state[0][5]],
        [state[0][4], state[1][3], state[2][2], state[3][1], state[4][0]],
        [state[1][5], state[2][4], state[3][3], state[4][2], state[5][1]],
        # Hàng Chéo Bên Phải
        [state[0][0], state[1][1], state[2][2], state[3][3], state[4][4]],
        [state[1][1], state[2][2], state[3][3], state[4][4], state[5][5]],
        [state[0][1], state[1][2], state[2][3], state[3][4], state[4][5]],
        [state[1][0], state[2][1], state[3][2], state[4][3], state[5][4]]
    ]
    if [player, player, player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]
    
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, player*-1)
        
       
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    
    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '------------------------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 36:
        x = choice([0, 1, 2, 3, 4, 5])
        y = choice([0, 1, 2, 3, 4, 5])
    elif depth > 9:
        move = ai_turn_upgrade(board)
        x, y = move[0], move[1]
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)
    
def ai_turn_upgrade(board):
    result = 0
    move = []
    h = 0
    c = 0
    for x in range(0,6):
        for y in range(0,6):
            count = 0
            if board[x][y] == 0:
                for i in range(0,6):
                    if board[x][i] == -1:
                        count += 0.5
                        h += 1 
                    elif board[x][i] == 1:
                        count += 1
                        c += 1
                if (h == 3 and c == 0) or h == 4:
                    return [x,y]
                elif c > 1 and h > 0 and (board[x][1] == -1 or board[x][2] == -1 or board[x][3] == -1 or board[x][4] == -1):
                    count -= 1
                h = 0
                c = 0
                for i in range(0,6):
                    if board[i][y] == -1:
                        count += 0.5
                        h += 1
                    elif board[i][y] == 1:
                        count += 1
                        c += 1
                if (h == 3 and c == 0) or h == 4:
                    return [x,y]
                elif c > 1 and h > 0 and (board[1][y] == -1 or board[2][y] == -1 or board[3][y] == -1 or board[4][y] == -1):
                    count -= 1
                h = 0
                c = 0
                if [x,y] in [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]:
                    for i in [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]:
                        if board[i[0]][i[1]] == -1:
                            count += 0.5
                            h += 1
                        elif board[i[0]][i[1]] == 1:
                            count += 1
                            c += 1
                    if (h == 3 and c == 0) or h == 4:
                       return [x,y]
                    elif c > 1 and h > 0 and (board[1][1] == -1 or board[2][2] == -1 or board[3][3] == -1 or board[4][4] == -1):
                        count -= 1
                    h = 0
                    c = 0
                if [x,y] in [[0,5],[1,4],[2,3],[3,2],[4,1],[5,0]]:
                    for i in [[0,5],[1,4],[2,3],[3,2],[4,1],[5,0]]:
                        if board[i[0]][i[1]] == -1:
                            count += 0.5
                            h += 1
                        elif board[i[0]][i[1]] == 1:
                            count += 1
                            c += 1
                    if (h == 3 and c == 0) or h == 4:
                        return [x,y]
                    elif c > 1 and h > 0 and (board[1][4] == -1 or board[2][3] == -1 or board[3][2] == -1 or board[4][1] == -1):
                        count -= 1
                    h = 0
                    c = 0
                if [x,y] in [[0,1],[1,2],[2,3],[3,4],[4,5]]:
                    for i in [[0,1],[1,2],[2,3],[3,4],[4,5]]:
                        if board[i[0]][i[1]] == -1:
                            count += 0.5
                            h += 1
                        elif board[i[0]][i[1]] == 1:
                            count += 1
                    if h == 4:
                        return [x,y]
                    elif h > 0:
                        count -= 1
                    h = 0
                if [x,y] in [[1,0],[2,1],[3,2],[4,3],[5,4]]:
                    for i in [[1,0],[2,1],[3,2],[4,3],[5,4]]:
                        if board[i[0]][i[1]] == -1:
                            count += 0.5
                            h += 1
                        elif board[i[0]][i[1]] == 1:
                            count += 1
                    if h == 4:
                        return [x,y]
                    elif h > 0:
                        count -= 1
                    h = 0
                if [x,y] in [[0,4],[1,3],[2,2],[3,1],[4,0]]:
                    for i in [[0,4],[1,3],[2,2],[3,1],[4,0]]:
                        if board[i[0]][i[1]] == -1:
                            count += 0.5
                            h += 1
                        elif board[i[0]][i[1]] == 1:
                            count += 1
                    if h == 4:
                        return [x,y]
                    elif h > 0:
                        count -= 1
                    h = 0
                if [x,y] in [[1,5],[2,4],[3,3],[4,2],[5,1]]:
                    for i in [[1,5],[2,4],[3,3],[4,2],[5,1]]:
                        if board[i[0]][i[1]] == -1:
                            count += 0.5
                            h += 1
                        elif board[i[0]][i[1]] == 1:
                            count += 1
                    if h == 4:
                        return [x,y]
                    elif h > 0:
                        count -= 1
                    h = 0
                if count >= result:
                    result = count
                    move = [x,y]       
    return move

def human_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3], 5: [0, 4], 6: [0, 5],
        7: [1, 0], 8: [1, 1], 9: [1, 2], 10: [1, 3], 11: [1, 4], 12: [1, 5],
        13: [2, 0], 14: [2, 1], 15: [2, 2], 16: [2, 3], 17: [2, 4], 18: [2, 5],
        19: [3, 0], 20: [3, 1], 21: [3, 2], 22: [3, 3], 23: [3, 4], 24: [3, 5],
        25: [4, 0], 26: [4, 1], 27: [4, 2], 28: [4, 3], 29: [4, 4], 30: [4, 5],
        31: [5, 0], 32: [5, 1], 33: [5, 2], 34: [5, 3], 35: [5, 4], 36: [5, 5]
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 36:
        try:
            move = int(input('Use numpad (1..36): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

        # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''
        
        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
