import pygame
import sys

# Dimensiones del tablero
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4,4
SQUARE_SIZE = WIDTH // COLS

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Movimientos posibles del caballo
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
    # Marcar la casilla actual como visitada
    board[x][y] = move_count
    
    # Dibujar el tablero y el recorrido del caballo en la pantalla
    draw_board(screen)
    draw_knights_tour(screen, board)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Pequeña pausa para visualización
    pygame.time.delay(500)
    
    # Comprobar si se ha completado el recorrido
    if move_count == ROWS * COLS:
        # Pausa adicional después de completar el recorrido
        pygame.time.delay(3000)
        
        # Cerrar Pygame y salir del programa
        pygame.quit()
        sys.exit()

    # Explorar los posibles movimientos del caballo
    for k in range(8):
        next_x, next_y = x + MOVE_X[k], y + MOVE_Y[k]
        
        # Verificar si el movimiento es válido y la casilla no ha sido visitada
        if is_valid_move(next_x, next_y) and board[next_x][next_y] == -1:
            # Llamada recursiva para el siguiente movimiento
            if knights_tour_dfs(screen, board, next_x, next_y, move_count + 1):
                return True

    # Si no hay movimientos válidos desde la posición actual, retroceder (backtrack)
    board[x][y] = -1
    
    # Redibujar el tablero y el recorrido del caballo
    draw_board(screen)
    draw_knights_tour(screen, board)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Pequeña pausa para visualización
    pygame.time.delay(500)
    
    # Indicar que no se ha encontrado una solución desde esta posición
    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Knight's Tour")

    board = create_board()

    # Starting position
    start_x, start_y = 0, 0
    knights_tour_dfs(screen, board, start_x, start_y, 0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

