import pygame
import sys

from settings import *
from game import check_win
from board import (
    draw_lines,
    make_move,
    restart,
    draw_win_line,
    is_board_full
)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

draw_lines(screen)

player = 1
game_over = False
font = pygame.font.Font(None, 40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if is_board_full():
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            make_move(screen, event, player)
            result = check_win(player)

            if result:
                win_type, index = result
                draw_win_line(screen, win_type, index)
                game_over = True

            player = 3 - player

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart(screen)
                game_over = False

        if game_over:
            restart_message = font.render("Press R to restart", True, (0, 0, 139))
            screen.blit(restart_message, (WIDTH // 4 + 40, HEIGHT // 2))

    pygame.display.update()
