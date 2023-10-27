import heapq
from Nodo import Nodo

class Busquedas:

    #Constructor, recibe como parametro el laberinto que se desea explorar
    def __init__(self, labarinto, inicio, meta):
        self.laberinto = labarinto
        self.inicio = inicio
        self.meta = meta

    def costo_uniforme_modificado(self):
        inicio = self.inicio
        meta = self.meta
        cola_prioridad = [Nodo(inicio, 0, 0)]
        nodos_expandidos = set()
        ramas_olvidadas = {}
        laberinto = self.laberinto
        while cola_prioridad:
            nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual.estado == meta:
                return reconstruir_camino(nodo_actual)

            nodos_expandidos.add(nodo_actual.estado)

            for accion, siguiente_estado, costo in expandir_nodo(nodo_actual, laberinto):
                costo_acumulado = nodo_actual.costo_acumulado + costo
                if siguiente_estado not in nodos_expandidos:
                    if siguiente_estado in ramas_olvidadas:
                        if costo_acumulado < ramas_olvidadas[siguiente_estado]:
                            ramas_olvidadas[siguiente_estado] = costo_acumulado
                            # Re-expande la rama
                            for index, nodo in enumerate(cola_prioridad):
                                if nodo.estado == siguiente_estado:
                                    cola_prioridad.pop(index)
                                    break
                        else:
                            continue

                    heapq.heappush(cola_prioridad, Nodo(siguiente_estado, costo, costo_acumulado, nodo_actual))
                    ramas_olvidadas[siguiente_estado] = costo_acumulado

        return None  # No se encontró una solución


    #Busqueda A*
    def astar(self):
        inicio = self.inicio
        objetivo = self.meta
        lista_abierta = [(0, inicio)]  # Prioridad y posición del nodo de inicio
        vino_de = {}
        g_puntaje = {inicio: 0}
        grid = self.laberinto



        while lista_abierta:
            # Ordenar la lista de nodos abiertos por el menor costo
            lista_abierta.sort()
            costo_actual, nodo_actual = lista_abierta.pop(0)

            if nodo_actual == objetivo:
                # Reconstruir el camino y devolverlo
                camino = []
                while nodo_actual in vino_de:
                    camino.insert(0, nodo_actual)
                    nodo_actual = vino_de[nodo_actual]
                return camino, g_puntaje

            for vecino in obtener_vecinos(nodo_actual, grid):
                x, y = vecino
                # Costo unitario de movimiento
                costo = 1
                if grid[x][y] == 3:  # "Justo" reduce el costo acumulado en 2
                    costo -= 2
                elif grid[x][y] == 4:  # "Gato malvado" aumenta el costo acumulado en 3
                    costo += 3

                puntaje_g_tentativo = g_puntaje[nodo_actual] + costo

                if vecino not in g_puntaje or puntaje_g_tentativo < g_puntaje[vecino]:
                    g_puntaje[vecino] = puntaje_g_tentativo
                    puntaje_f = puntaje_g_tentativo + heurística(vecino, objetivo)
                    if vecino not in [elemento[1] for elemento in lista_abierta]:
                        lista_abierta.append((puntaje_f, vecino))
                    vino_de[vecino] = nodo_actual



        return None  # No se encontró un camino

def heurística(nodo, objetivo):
    x1, y1 = nodo
    x2, y2 = objetivo
    return abs(x1 - x2) + abs(y1 - y2)

def obtener_vecinos(nodo, grid):
    x, y = nodo
    vecinos = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]  # Movimientos arriba, abajo, izquierda, derecha
    vecinos_válidos = []
    for vecino in vecinos:
        nx, ny = vecino
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            vecinos_válidos.append(vecino)
    return vecinos_válidos


def expandir_nodo(nodo, laberinto):
    acciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Movimientos posibles (arriba, derecha, abajo, izquierda)
    sucesores = []

    for dx, dy in acciones:
        x, y = nodo.estado
        nuevo_x, nuevo_y = x + dx, y + dy

        if 0 <= nuevo_x < len(laberinto) and 0 <= nuevo_y < len(laberinto[0]) and laberinto[nuevo_x][nuevo_y] != 1:
            costo = 1
            if laberinto[nuevo_x][nuevo_y] == 3:
                costo = -2
            elif laberinto[nuevo_x][nuevo_y] == 4:
                costo = 3

            sucesores.append((f'Mover a ({nuevo_x}, {nuevo_y})', (nuevo_x, nuevo_y), costo))

    return sucesores


def reconstruir_camino(nodo):
    camino = []
    costo_total = 0
    while nodo:
        camino.insert(0, (nodo.estado, nodo.costo_acumulado))
        nodo = nodo.padre
    return camino

