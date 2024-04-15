import numpy as np


def find_next_row(rack, col):
    for row in range(len(rack) - 1, -1, -1):
        if rack[row][col] == 0:
            return row


def put_piece(rack, row, col, piece):
    rack[row][col] = piece
    print(rack)


def check_valid(rack, row, col):
    if rack[row][col] == 0:
        return True
    else:
        return False


def check_winning(rack, piece):
    # Horizontal locations
    for c in range(col_num - 3):
        for r in range(row_num):
            if (rack[r][c] == piece and rack[r][c + 1] == piece and rack[r][c + 2] == piece and
                    rack[r][c + 3] == piece):
                return True

    # Vertical locations
    for c in range(col_num):
        for r in range(row_num - 3):
            if (rack[r][c] == piece and rack[r + 1][c] == piece and rack[r + 2][c] == piece and
                    rack[r + 3][c] == piece):
                return True

    # Positively sloped diaganols
    for c in range(col_num - 3):
        for r in range(row_num - 3):
            if (rack[r][c] == piece and rack[r + 1][c + 1] == piece and rack[r + 2][c + 2] == piece and
                    rack[r + 3][c + 3] == piece):
                return True

    # Negatively sloped diaganols
    for c in range(col_num - 3):
        for r in range(3, row_num):
            if (rack[r][c] == piece and rack[r - 1][c + 1] == piece and rack[r - 2][c + 2] == piece and
                    rack[r - 3][c + 3] == piece):
                return True


def winner(turn, starter):
    print("Yay!")
    print("Player", turn, "won.")
    answer = input("Wanna play again? y/n: ")
    if answer == 'y':
        print("Welcome Back")
        if starter == 0:
            next_player = 1
        else:
            next_player = 0
        print("This time player", next_player + 1, "will be the starter.")
        new_rack = np.zeros((5, 5), dtype=int)
        game(new_rack, next_player)
    else:
        print("Good Bye.")
        print("Come By Soon ;) ")
        exit(0)

def check_draw(rack):
    for row in rack:
        if 0 in row:
            return False
    return True  # Rack is filled

def check_move(rack, turn, col, starter):
    if col < col_num:
        row = find_next_row(rack, col)
        if check_valid(rack, row, col):
            put_piece(rack, row, col, turn)
            if check_winning(rack, turn):
                winner(turn, starter)

        else:
            print("Invalid Move!")

    else:
        print("Invalid Move!")
        exit(0)


def game(rack, turn):
    starter = turn

    while run:

        if turn == 0:
            col = int(input("Player 1:"))
            check_move(rack, 1, col, starter)

        elif turn == 1:
            col = int(input("Player 2:"))
            check_move(rack, 2, col, starter)

        turn = (turn + 1) % 2

        if check_draw(rack):
            print("DRAW!")
            exit(0)


run = True
col_num = 5
row_num = 5
turn = 0
rack = np.zeros((row_num, col_num), dtype=int)
game(rack, turn)
