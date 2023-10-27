import tkinter as tk
from UI.mazeInterface import display_maze
from UI.selectAlgorithm import seleccionar_algoritmo
from busquedas import Busquedas

laberinto = \
    [[0, 0, 0, 3, 0, 0, 0, 0],
     [0, 3, 1, 1, 4, 1, 1, 0],
     [0, 1, 0, 4, 4, 1, 1, 0],
     [0, 1, 0, 1, 1, 1, 1, 0],
     [0, 3, 0, 4, 0, 1, 0, 0]]


# Create a tkinter window
root = tk.Tk()

# Set the size of the window
root.geometry("350x350")

# Create two labels for the input fields
inicio_label = tk.Label(root, text="Inicio (fila,columna):")
meta_label = tk.Label(root, text="Meta (fila,columna):")

# Create two entry widgets for inputting the start and end positions
inicio_entry = tk.Entry(root)
meta_entry = tk.Entry(root)

# Create a function to update the start and end positions based on the entry widget values
def update_positions():
    global inicio, meta
    inicio = tuple(map(int, inicio_entry.get().split(',')))
    meta = tuple(map(int, meta_entry.get().split(',')))
    costo_uniforme = Busquedas(laberinto, inicio, meta).costo_uniforme_modificado()
    astar = Busquedas(laberinto, inicio, meta).astar()
    costo_uniforme_parsed = [tupla[0] for tupla in costo_uniforme]
    costo_uniforme_peso = [tupla[1] for tupla in costo_uniforme]
    astar_parsed = astar[0]
    astar_peso = [value for value in astar[1].values() if isinstance(value, int)]
    algo = seleccionar_algoritmo()
    if algo == "Costo Uniforme Modificado":
        print("Costo peso: ", costo_uniforme_peso)
        print("Costo Ruta: ", costo_uniforme_parsed)
        display_maze(laberinto, inicio, meta, costo_uniforme_parsed.copy(), algo, costo_uniforme_peso)
    elif algo == "A*":
        print(astar)
        print("Astar peso: ", set(astar_peso))
        print("Astar Ruta: ", astar_parsed)
        display_maze(laberinto, inicio, meta, astar_parsed.copy(), algo, set(astar_peso))

# Create a button to update the positions
update_button = tk.Button(root, text="Update Positions", command=update_positions)

# Pack the widgets into the window
inicio_label.pack(anchor="center", pady=10)
inicio_entry.pack(anchor="center", pady=10)
meta_label.pack(anchor="center", pady=10)
meta_entry.pack(anchor="center", pady=10)
update_button.pack(anchor="center", pady=10)

# Start the tkinter event loop
root.mainloop()