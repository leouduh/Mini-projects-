import random
import pygame
import numpy as np
import time as t

# initialize pygame
pygame.init()
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
NAVY = (0, 0, 128)
LIME = (0, 255, 0)

color_pool = [OLIVE, PURPLE, MAROON, NAVY, LIME]


BLACK = (0, 0, 0)
MAGENTA = (0, 0, 128)
TEAL = (0, 128, 128)
MAROON = (128, 0, 0)
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_RADIUS = 50
CIRCLE_WIDTH = 10
X_WIDTH = 10
X_COLOR = GREY = (128, 128, 128)
WIN_LINE_WIDTH = 8
ACCOMMODATION_X = 50
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tictactoe.png")
pygame.display.set_icon(icon)
player_color = None
player_1_text = "O"
player_2_text = "X"
text_surface = None
clock = pygame.time.Clock()
text = "yes"

screen.fill(random.choice(color_pool))
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
player = 1

# creating font


def draw_figure():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row, col] == 1:
                pygame.draw.circle(screen, TEAL, ((col * 200 + 100), (row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row, col] == 2:
                pygame.draw.line(screen, X_COLOR, ((col * 200 + ACCOMMODATION_X), (row * 200 + 200 - ACCOMMODATION_X)),
                                 ((col * 200 + 200 - ACCOMMODATION_X), (row * 200 + ACCOMMODATION_X)), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, ((col * 200 + ACCOMMODATION_X), (row * 200 + ACCOMMODATION_X)),
                                 ((col * 200 + 200 - ACCOMMODATION_X), (row * 200 + 200 - ACCOMMODATION_X)), X_WIDTH)


def mark_square(row, col, player_param):
    global board
    board[row, col] = player_param


def is_square_available(row, col):
    return board[row, col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row, col] == 0:
                return False
    return True


def draw_lines():
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), width=10)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), width=10)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), width=10)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), width=10)


def check_for_win(player_param):

    for col in range(BOARD_COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player_param)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player_param)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_first_diagonal_win_line(player)
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        draw_sc_diagonal_win_line(player)
        return True


def draw_vertical_win_line(col, player_param):
    global player_color
    if player_param == 1:
        player_color = TEAL
    elif player_param == 2:
        player_color = X_COLOR
    pygame.draw.line(screen, player_color, (col * 200 + 100, 25), (col * 200 + 100, 575), WIN_LINE_WIDTH)


def draw_horizontal_win_line(row, player_param):
    global player_color
    if player_param == 1:
        player_color = TEAL
    elif player_param == 2:
        player_color = X_COLOR
    pygame.draw.line(screen, player_color, (25, row * 200 + 100), (575, row * 200 + 100), WIN_LINE_WIDTH)


def draw_first_diagonal_win_line(player_param):
    global player_color
    if player_param == 1:
        player_color = TEAL
    elif player_param == 2:
        player_color = X_COLOR
    pygame.draw.line(screen, player_color, (0 + 50, 0 + 50), (600 - 50, 600 - 50), WIN_LINE_WIDTH)


def draw_sc_diagonal_win_line(player_param):
    global player_color
    if player_param == 1:
        player_color = TEAL
    elif player_param == 2:
        player_color = X_COLOR
    pygame.draw.line(screen, player_color, (600 - 50, 0 + 50), (0 + 50, 600 - 50), WIN_LINE_WIDTH)


def reset_the_board(text_param):
    global player, text_surface, board, text
    text_rect = text_param.get_rect()
    text_rect.center = (300, 300)
    screen.blit(text, text_rect)
    pygame.display.update()
    t.sleep(0.5)
    screen.fill(random.choice(color_pool))
    draw_lines()
    player = 1
    board = np.zeros((3, 3))


def restart_game():
    global player, text_surface, board, text
    screen.fill(MAGENTA)
    font = pygame.font.Font('freesansbold.ttf', 50)
    if player == 1:
        text = font.render(f"{player_2_text} WINS", True, BLACK)
    elif player == 2:
        text = font.render(f"{player_1_text} WINS", True, BLACK)
    reset_the_board(text)


def rester():
    global player, board
    board = np.zeros((3, 3))


def check_if_there_is_zero():
    global BOARD_COLUMNS
    global BOARD_ROWS
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row, col] != 0:
                return False
    return True


def check_for_draw():
    global player, text_surface, board, text
    if np.all(board) == True:
        screen.fill(MAGENTA)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render("DRAW!!!!", True, BLACK)
        reset_the_board(text)
        return True


draw_lines()
running = True
game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY//200
            clicked_col = mouseX//200
            if is_square_available(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, player)
                    if check_for_win(player):
                        game_over = True
                    elif check_for_draw():
                        game_over = False
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, player)
                    if check_for_win(player):
                        game_over = True
                    elif check_for_draw():
                        game_over = False
                    player = 1
                draw_figure()
                pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart_game()
                game_over = False
    pygame.display.update()












