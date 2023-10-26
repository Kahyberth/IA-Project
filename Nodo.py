class Nodo:
    def __init__(self, estado, costo, costo_acumulado, padre=None):
        self.estado = estado
        self.costo = costo
        self.costo_acumulado = costo_acumulado
        self.padre = padre
        self.hijos = []

    def __lt__(self, otro):
        return self.costo_acumulado < otro.costo_acumulado