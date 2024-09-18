import pygame

from settings import *

board = [[0 for _ in range(3)] for _ in range(3)]


def draw_lines(screen):
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures(screen):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


def get_center(index, size):
    return index * size + size // 2


def draw_win_line(screen, win_type, index):
    padding = 15

    if win_type == "row":
        y = get_center(index, SQUARE_SIZE)
        start_position = (padding, y)
        end_position = (WIDTH - padding, y)

    elif win_type == "column":
        x = get_center(index, SQUARE_SIZE)
        start_position = (x, padding)
        end_position = (x, HEIGHT - padding)

    elif win_type == "diagonal":
        if index == 1:
            start_position = (padding, padding)
            end_position = (WIDTH - padding, HEIGHT - padding)
        elif index == 2:
            start_position = (WIDTH - padding, padding)
            end_position = (padding, HEIGHT - padding)

    pygame.draw.line(screen, RED, start_position, end_position, LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def make_move(screen, event, player):
    mouseX = event.pos[0]
    mouseY = event.pos[1]

    clicked_row = mouseY // SQUARE_SIZE
    clicked_col = mouseX // SQUARE_SIZE

    print(clicked_row)
    print(clicked_col)

    if is_square_empty(clicked_row, clicked_col):
        mark_square(clicked_row, clicked_col, player)
        draw_figures(screen)
        return 1

    draw_figures(screen)
    return 0


def is_square_empty(row, col):
    return board[row][col] == 0


def is_board_full():
    return not any(0 in row for row in board)


def restart(screen):
    screen.fill(BG_COLOR)
    draw_lines(screen)
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
