from busquedas import Busquedas

laberinto = \
    [[0, 0, 4, 0, 0, 0, 0, 0],
     [0, 3, 1, 1, 3, 1, 1, 0],
     [0, 1, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 0],
     [0, 3, 0, 4, 0, 0, 0, 0]]

inicio = (2, 7)
meta = (2, 0)


ruta = Busquedas(laberinto).costo_uniforme_modificado(inicio,meta)
print("Costo recursivo: ", ruta)


astar = Busquedas(laberinto).astar(inicio,meta)

print("Print Astar: ", astar)


