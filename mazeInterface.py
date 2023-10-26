import pygame
import sys
from maze import Maze

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
            if characters == 1: #Agente
                screen.blit(agente_image, (x, y))
            if characters == 4: #Katz
                screen.blit(katz_image, (x, y))
            if characters == 5: #Muriel
                screen.blit(muriel_image, (x, y))
            if characters == 3: #Justo
                screen.blit(justo_image, (x, y))
            if characters == 2: #Obstaculo
                screen.blit(obstacle_image, (x,y))


# Bucle principal (Mantiene la pantalla hasta que se cierre)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el tablero
    dibujar_tablero(matriz)

    # Actualizar la pantalla
    pygame.display.update()
