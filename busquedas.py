import heapq
from Nodo import Nodo

class Busquedas:
    def costo_uniforme_modificado(inicio, meta, laberinto):
        cola_prioridad = [Nodo(inicio, 0, 0)]
        nodos_expandidos = set()
        ramas_olvidadas = {}

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

