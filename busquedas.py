import heapq
from Nodo import Nodo

class Busquedas:

    #Constructor, recibe como parametro el laberinto que se desea explorar
    def __init__(self, labarinto):
        self.laberinto = labarinto

    def costo_uniforme_modificado(self, inicio, meta):
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
    def astar(self, start, goal):
        open_list = [(0, start)]  # Prioridad y posición del nodo de inicio
        came_from = {}
        g_score = {start: 0}
        grid = self.laberinto

        while open_list:
            open_list.sort()
            current_cost, current_node = open_list.pop(0)

            if current_node == goal:
                path = []
                while current_node in came_from:
                    path.insert(0, current_node)
                    current_node = came_from[current_node]
                return path

            for neighbor in get_neighbors(current_node, grid):
                x, y = neighbor
                # Coste unitario de movimiento
                cost = 1
                if grid[x][y] == 3:  # Justo disminuye el costo acumulado en 2
                    cost -= 2
                elif grid[x][y] == 4:  # Gato malvado aumenta el costo acumulado en 3
                    cost += 3

                tentative_g_score = g_score[current_node] + cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)

                    if neighbor not in [item[1] for item in open_list]:
                        open_list.append((f_score, neighbor))
                    came_from[neighbor] = current_node

        return None  # No se encontró un camino

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(node, grid):
    x, y = node
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]  # Movimientos arriba, abajo, izquierda, derecha
    valid_neighbors = []
    for neighbor in neighbors:
        nx, ny = neighbor
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            valid_neighbors.append(neighbor)
    return valid_neighbors


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

