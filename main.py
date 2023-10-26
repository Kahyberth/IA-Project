from busquedas import Busquedas

laberinto = \
    [[0, 0, 4, 0, 0, 0, 0, 0],
     [0, 3, 1, 1, 3, 1, 1, 0],
     [0, 1, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 0],
     [0, 3, 0, 4, 0, 0, 0, 0]]

inicio = (2, 7)
meta = (2, 0)

ruta = Busquedas.costo_uniforme_modificado(inicio, meta, laberinto)

counter = 0
for i in ruta:
    counter +=1
    print(f"Paso: {counter} ", i)