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


def draw_win_line(screen, win_type, index):
    if win_type == "row":
        start_position = (15, index * SQUARE_SIZE + SQUARE_SIZE // 2)
        end_position = (WIDTH - 15, index * SQUARE_SIZE + SQUARE_SIZE // 2)

    elif win_type == "column":
        start_position = (index * SQUARE_SIZE + SQUARE_SIZE // 2, 15)
        end_position = (index * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 15)

    elif win_type == "diagonal" and index == 1:
        start_position = (15, 15)
        end_position = (WIDTH - 15, HEIGHT - 15)

    elif win_type == "diagonal" and index == 2:
        start_position = (WIDTH - 15, 15)
        end_position = (15, HEIGHT - 15)

    pygame.draw.line(screen, RED, start_position, end_position, LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def make_move(screen, event, player):
    mouseX = event.pos[0]
    mouseY = event.pos[1]

    clicked_row = mouseY // SQUARE_SIZE
    clicked_col = mouseX // SQUARE_SIZE

    if is_square_empty(clicked_row, clicked_col):
        mark_square(clicked_row, clicked_col, player)
        draw_figures(screen)


def is_square_empty(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True


def restart(screen):
    screen.fill(BG_COLOR)
    draw_lines(screen)
    for row in range(3):
        for col in range(3):
            board[row][col] = 0
