import time

import pygame
import sys


# Definir las dimensiones del tablero
rows, columns = 5, 8
cell_width = 100

# Configurar Pygame
pygame.init()

# Definir el tamaño de la ventana
screen_width = columns * cell_width
screen_height = rows * cell_width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agente Coraje")

# Definir las imagenes de los personajes
agente_image = pygame.image.load("Resources\Coraje.png")
muriel_image = pygame.image.load("Resources\Muriel.png")
justo_image = pygame.image.load("Resources\Justo.png")
katz_image = pygame.image.load("Resources\Katz.png")
obstacle_image = pygame.image.load("Resources\Obstaculo.png")

matriz_prueba = [
    [0, 0, 0, 4, 0, 0, 0, 0],
    [0, 3, 2, 2, 3, 2, 2, 0],
    [5, 2, 0, 0, 0, 2, 2, 1],
    [0, 2, 0, 2, 2, 2, 0, 0],
    [0, 3, 0, 4, 0, 0, 0, 0]
]

# Definir la posición inicial del agente
posicion_agente = [2, 7]

# Crear una instancia de la clase Maze
#maze = Maze()
matriz = matriz_prueba  # Obtener la matriz del laberinto

# Función para dibujar el tablero con divisiones de celdas
def dibujar_tablero(matriz):
    for fila in range(rows):
        for columna in range(columns):
            color_celda = (255, 255, 255)  # Color blanco para las celdas
            x = columna * cell_width
            y = fila * cell_width
            pygame.draw.rect(screen, color_celda, (x, y, cell_width, cell_width))

            color_borde = (0, 0, 0)  # Color negro para los bordes
            grosor_borde = 2  # Grosor del borde
            pygame.draw.rect(screen, color_borde, (x, y, cell_width, cell_width), grosor_borde)

            characters = matriz[fila][columna]
            if characters == 1:  # Agente
                x_agente = x + cell_width // 2  # Posición X del centro de la celda
                y_agente = y + cell_width // 2  # Posición Y del centro de la celda
                screen.blit(agente_image,
                             (x_agente - agente_image.get_width() // 2, y_agente - agente_image.get_height() // 2))
            if characters == 4: #Katz
                screen.blit(katz_image, (x, y))
            if characters == 5: #Muriel
                screen.blit(muriel_image, (x, y))
            if characters == 3: #Justo
                screen.blit(justo_image, (x, y))
            if characters == 2: #Obstaculo
                screen.blit(obstacle_image, (x,y))

# Camino prueba
pathfinder = [(2, 7), (3, 7), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0)]

# Bucle principal (Mantiene la pantalla hasta que se cierre)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pathfinder:
        nueva_posicion = pathfinder.pop(0)
        x1, y1 = posicion_agente
        x2, y2 = nueva_posicion

        # Animación del movimiento del agente
        for i in range(10):  # Realiza 10 pasos para la animación
            inter_x = x1 + (x2 - x1) * i / 10
            inter_y = y1 + (y2 - y1) * i / 10
            matriz[x1][y1] = 0
            matriz[int(inter_x)][int(inter_y)] = 1
            dibujar_tablero(matriz)
            pygame.display.update()
            time.sleep(0.1)

        matriz[x1][y1] = 0
        matriz[x2][y2] = 1
        posicion_agente = nueva_posicion

    # Dibujar el tablero
    dibujar_tablero(matriz)

    # Actualizar la pantalla
    pygame.display.update()
