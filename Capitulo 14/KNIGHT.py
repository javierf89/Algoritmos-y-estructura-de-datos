import pygame
import sys

# Dimensiones del tablero
ANCHO, ALTO = 600, 600
FILAS, COLUMNAS = 4, 4
TAMANO_CUADRO = ANCHO // COLUMNAS

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Movimientos posibles del caballo
MOVIMIENTO_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOVIMIENTO_Y = [1, 2, 2, 1, -1, -2, -2, -1]

def crear_tablero():
    return [[-1 for _ in range(COLUMNAS)] for _ in range(FILAS)]

def es_movimiento_valido(x, y):
    return 0 <= x < COLUMNAS and 0 <= y < FILAS

def dibujar_tablero(pantalla):
    pantalla.fill(BLANCO)
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            color = BLANCO if (fila + col) % 2 == 0 else NEGRO
            pygame.draw.rect(pantalla, color, (col * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))

def dibujar_recorrido_caballo(pantalla, tablero):
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            if tablero[fila][col] != -1:
                pygame.draw.circle(pantalla, VERDE, (col * TAMANO_CUADRO + TAMANO_CUADRO // 2, fila * TAMANO_CUADRO + TAMANO_CUADRO // 2), 20)

def recorrido_caballo_dfs(pantalla, tablero, x, y, contador_movimientos):
    # Marcar la casilla actual como visitada
    tablero[x][y] = contador_movimientos
    
    # Dibujar el tablero y el recorrido del caballo en la pantalla
    dibujar_tablero(pantalla)
    dibujar_recorrido_caballo(pantalla, tablero)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Pequeña pausa para visualización
    pygame.time.delay(500)
    
    # Comprobar si se ha completado el recorrido
    if contador_movimientos == FILAS * COLUMNAS:
        # Pausa adicional después de completar el recorrido
        pygame.time.delay(3000)
        
        # Cerrar Pygame y salir del programa
        pygame.quit()
        sys.exit()

    # Explorar los posibles movimientos del caballo
    for k in range(8):
        siguiente_x, siguiente_y = x + MOVIMIENTO_X[k], y + MOVIMIENTO_Y[k]
        
        # Verificar si el movimiento es válido y la casilla no ha sido visitada
        if es_movimiento_valido(siguiente_x, siguiente_y) and tablero[siguiente_x][siguiente_y] == -1:
            # Llamada recursiva para el siguiente movimiento
            if recorrido_caballo_dfs(pantalla, tablero, siguiente_x, siguiente_y, contador_movimientos + 1):
                return True

    # Si no hay movimientos válidos desde la posición actual, retroceder (backtrack)
    tablero[x][y] = -1
    
    # Redibujar el tablero y el recorrido del caballo
    dibujar_tablero(pantalla)
    dibujar_recorrido_caballo(pantalla, tablero)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Pequeña pausa para visualización
    pygame.time.delay(500)
    
    # Indicar que no se ha encontrado una solución desde esta posición
    return False

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Recorrido del Caballo")

    tablero = crear_tablero()

    # Posición inicial
    inicio_x, inicio_y = 0, 0
    recorrido_caballo_dfs(pantalla, tablero, inicio_x, inicio_y, 0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

