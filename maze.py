import numpy as np
import random
class Maze:
    def __int__(self):
        pass

    # Genera un laberinto aleatorio
    def generate_maze(self, grid = np.zeros((5, 8))):
        grid # Por default genera una matriz de 5X8 con ceros
        data = np.array([])
        print("Matriz inicial: \n", grid)
        x1 = random.randint(0, 4)
        y1 = random.randint(0, 7)
        data = np.append(data,[x1,y1])
        print("Meta: ", "[", x1, ",", y1, "]")
        counter = 0
        while True:
            x2 = random.randint(0, 4)
            y2 = random.randint(0, 7)
            # Comprueba si la posicion de la meta no es igual a la posicion de inicio
            if x1 != x2 and y1 != y2:
                print("Agente: ", "[", x2, ",", y2, "]")
                data = np.append(data, [x2,y2])
                while True: #Se encarga de ubicar a justo en la matriz
                    x3 = random.randint(0, 4)
                    y3 = random.randint(0, 7)
                    if x3 != x2 and y3 != y2 and x3 != x1 and y3 != y1 and not np.array_equal(data, [x3, y3]):
                        grid[x3,y3] = 3 #Abusador ( Amo )
                        print("Abusador: ", "[", x3, ",", y3, "]")
                        data = np.append(data, [x2, y2])
                        counter += 1
                        if counter == 3:
                            break
                grid[x1,y1] = 5 #Muriel ( Meta )
                grid[x2,y2] = 1 #Coraje ( Agente )
                break
        print("Matriz actualizada: \n", grid)

maze = Maze()
matriz = maze.generate_maze()
print(matriz)










