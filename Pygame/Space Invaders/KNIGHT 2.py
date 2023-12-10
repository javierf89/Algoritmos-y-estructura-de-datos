import pygame
import sys

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 5, 5
SQUARE_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

MOVE_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOVE_Y = [1, 2, 2, 1, -1, -2, -2, -1]

def create_board():
    return [[-1 for _ in range(COLS)] for _ in range(ROWS)]

def is_valid_move(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS

def draw_board(screen):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_knights_tour(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != -1:
                pygame.draw.circle(screen, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)

def knights_tour_dfs(screen, board, x, y, move_count):
    board[x][y] = move_count
    draw_board(screen)
    draw_knights_tour(screen, board)
    pygame.display.flip()
    pygame.time.delay(100)  # A small delay for visualization

    if move_count == ROWS * COLS:
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    # Aplicar la heurística de Warnsdorff para ordenar los movimientos
    next_moves = sorted([(x + MOVE_X[k], y + MOVE_Y[k]) for k in range(8) if is_valid_move(x + MOVE_X[k], y + MOVE_Y[k]) and board[x + MOVE_X[k]][y + MOVE_Y[k]] == -1],
                        key=lambda m: sum(1 for k in range(8) if is_valid_move(m[0] + MOVE_X[k], m[1] + MOVE_Y[k]) and board[m[0] + MOVE_X[k]][m[1] + MOVE_Y[k]] == -1))

    for move in next_moves:
        next_x, next_y = move
        if knights_tour_dfs(screen, board, next_x, next_y, move_count + 1):
            return True

    board[x][y] = -1
    draw_board(screen)
    draw_knights_tour(screen, board)
    pygame.display.flip()
    pygame.time.delay(100)
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Knight's Tour")

    board = create_board()

    start_x, start_y = 0, 0
    knights_tour_dfs(screen, board, start_x, start_y, 0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
