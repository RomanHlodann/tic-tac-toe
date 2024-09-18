from board import board


def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return 'row', row

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return 'column', col

    if board[0][0] == board[1][1] == board[2][2] == player:
        return 'diagonal', 1
    if board[0][2] == board[1][1] == board[2][0] == player:
        return 'diagonal', 2

    return False
