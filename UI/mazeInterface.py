import time

import pygame


def display_maze(matriz, inicio, meta, ruta, algoritmo, peso):

    pygame.init()

    # Dimension del tablero
    cell_width = 100
    rows = len(matriz)
    columns = len(matriz[0])
    indice_actual = 0
    peso = list(peso)


    screen_width = columns * cell_width + 300
    screen_height = rows * cell_width
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Agente Coraje")

    # Definir las imagenes de los personajes
    muriel_image = pygame.image.load("./Resources/Muriel.png")
    obstacle_image = pygame.image.load("./Resources/Obstaculo.png")
    agente_image = pygame.image.load("./Resources/Coraje.png")
    justo_image = pygame.image.load("./Resources/Justo.png")
    katz_image = pygame.image.load("./Resources/Katz.png")

    numbers_set = set()
    # Función para dibujar el tablero con divisiones de celdas
    def dibujar_tablero():
        for fila in range(rows):
            for columna in range(columns):
                color_celda = (5, 102, 8)  # Color blanco para las celdas
                x = columna * cell_width
                y = fila * cell_width
                pygame.draw.rect(screen, color_celda, (x, y, cell_width, cell_width))

                color_borde = (0, 0, 0)  # Color negro para los bordes
                grosor_borde = 2  # Grosor del borde
                pygame.draw.rect(screen, color_borde, (x, y, cell_width, cell_width), grosor_borde)

                #Dibuja los personajes y obstaculo
                characters = matriz[fila][columna]
                numbers_set.add(characters)
                if characters == 4:  # Katz
                    screen.blit(katz_image, (x, y))
                if characters == 2:  # Muriel
                    screen.blit(muriel_image, (x,y))
                if characters == 1:  # Obstaculo
                    screen.blit(obstacle_image, (x, y))
                if characters == 3:  # Justo
                    screen.blit(justo_image, (x, y))


    # Función para mostrar datos adicionales
    def mostrar_datos_adicionales(algoritmo):
        datos_font = pygame.font.Font(None, 32)

        if 0 <= indice_actual < len(peso):
            texto = datos_font.render("Peso acumulado: " + str(peso[indice_actual]), True, (255, 255, 255))
        else:
            texto = datos_font.render("Peso acumulado: "+str(peso[-1]), True, (255, 255, 255))

        x_texto = columns * cell_width + 10
        y_texto = 10
        screen.blit(texto, (x_texto, y_texto))

        texto = datos_font.render("Algoritmo: " + algoritmo, True, (255, 255, 255))
        y_texto += 50
        screen.blit(texto, (x_texto, y_texto))

    # Bucle principal (Mantiene la pantalla hasta que se cierre)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.quit()
                    return

        if ruta:
            nueva_posicion = ruta.pop(0)
            x1 = inicio[1] * cell_width
            y1 = inicio[0] * cell_width
            x2 = nueva_posicion[1] * cell_width
            y2 = nueva_posicion[0] * cell_width
            # Animación del movimiento del agente
            for i in range(0, cell_width, 5):
                screen.fill((0, 0, 0))
                dibujar_tablero()
                mostrar_datos_adicionales(algoritmo)
                screen.blit(muriel_image, (meta[1] * cell_width, meta[0] * cell_width))
                screen.blit(agente_image, (x1 + i * (x2 - x1) / cell_width, y1 + i * (y2 - y1) / cell_width))
                pygame.display.update()
                time.sleep(0.01)


            inicio = nueva_posicion
            indice_actual += 1
        else:
            screen.fill((0, 0, 0))
            dibujar_tablero()
            mostrar_datos_adicionales(algoritmo)
            screen.blit(agente_image, (x1 + i * (x2 - x1) / cell_width, y1 + i * (y2 - y1) / cell_width))
            pygame.display.update()