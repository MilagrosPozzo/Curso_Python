import numpy as np

# Crear un tablero de juego 5x5
def crearTablero():
    tablero = np.zeros((5,5))
    return tablero

# Colocar tres barcos en posiciones aleatorias
def ColocarBarcos(tablero):
    x, y = np.random.randint(0, 5, size=2)
    print(f"los valores de X e Y son {x} , {y}")
    tablero[x,y]=1

# Función para verificar si hay un barco o agua en las coordenadas dadas


# Prueba la función con algunas coordenadas


#Programa>> a JUGAR!
tabreal = crearTablero()
print("Tablero INICIAL\n")
print(tabreal)

ColocarBarcos(tabreal)
print("Tablero con BARCOS\n")
print(tabreal)