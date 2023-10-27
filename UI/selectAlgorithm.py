import pygame
import sys


def seleccionar_algoritmo():
    pygame.init()
    algoritmo_seleccionado = None
    # Definir el tamaño de la ventana de selección de algoritmo
    ventana_seleccion_ancho = 400
    ventana_seleccion_alto = 150
    ventana_seleccion = pygame.display.set_mode((ventana_seleccion_ancho, ventana_seleccion_alto))
    pygame.display.set_caption("Selección de Algoritmo")

    # Variables para la selección de algoritmo
    algoritmo_seleccionado = None

    # Bucle para la selección de algoritmo
    seleccionando_algoritmo = True
    while seleccionando_algoritmo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Seleccionar algoritmo 1
                    algoritmo_seleccionado = "Costo Uniforme Modificado"
                    seleccionando_algoritmo = False
                elif event.key == pygame.K_2:  # Seleccionar algoritmo 2
                    algoritmo_seleccionado = "A*"
                    seleccionando_algoritmo = False
                elif event.key == pygame.K_ESCAPE:  # Salir
                    pygame.quit()
                    sys.exit()

        # Dibuja la ventana de selección de algoritmo
        ventana_seleccion.fill((255, 255, 255))  # Fondo blanco
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Seleccione un algoritmo:", True, (0, 0, 0))
        ventana_seleccion.blit(texto, (10, 10))
        texto_1 = fuente.render("1 - Costo Uniforme Modificado", True, (0, 0, 0))
        ventana_seleccion.blit(texto_1, (10, 50))
        texto_2 = fuente.render("2 - A*", True, (0, 0, 0))
        ventana_seleccion.blit(texto_2, (10, 90))
        texto_3 = fuente.render("ESC - Salir", True, (0, 0, 0))
        ventana_seleccion.blit(texto_3, (10, 130))
        pygame.display.update()

    pygame.quit()
    return algoritmo_seleccionado
