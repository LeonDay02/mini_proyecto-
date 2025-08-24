import numpy as np
import random

# Función para colocar minas
def colocarMinas(campo, cantidad, orientacion="horizontal"):
    filas, columnas = campo.shape
    largo_mina = 3
    minas_colocadas = 0
    mina_id = 1

    while minas_colocadas < cantidad:
        if orientacion == "horizontal":
            fila = random.randint(0, filas - 1)
            col = random.randint(0, columnas - largo_mina)
            # Verificar si espacio está libre
            if np.all(campo[fila, col:col+largo_mina] == 0):
                campo[fila, col:col+largo_mina] = mina_id
                minas_colocadas += 1
                mina_id += 1

        elif orientacion == "vertical":
            fila = random.randint(0, filas - largo_mina)
            col = random.randint(0, columnas - 1)
            if np.all(campo[fila:fila+largo_mina, col] == 0):
                campo[fila:fila+largo_mina, col] = mina_id
                minas_colocadas += 1
                mina_id += 1

    return campo

# Función avance
def avance(campo, puntoInicio, puntoFin):
    puntos = 0
    fi, ci = puntoInicio
    ff, cf = puntoFin

    if campo[ff, cf] == 0:
        # buscar minas adyacentes al inicio
        for i in range(fi-1, fi+2):
            for j in range(ci-1, ci+2):
                if 0 <= i < campo.shape[0] and 0 <= j < campo.shape[1]:
                    if campo[i, j] != 0:
                        campo[i, j] = 0
                        puntos += 1
    else:
        # si hay mina en el punto final
        mina_id = campo[ff, cf]
        campo[campo == mina_id] = 0  # eliminar toda la mina
        puntos -= 3

    return puntos, campo

# Programa principal (demo)
if __name__ == "__main__":
    # Crear tablero vacío
    campo = np.zeros((10, 10), dtype=int)

    # Colocar 5 minas horizontalmente
    campo = colocarMinas(campo, 5, orientacion="horizontal")

    print("Tablero inicial:")
    print(campo)

    # Posición inicial aleatoria
    while True:
        start = (random.randint(0, 9), random.randint(0, 9))
        if campo[start] == 0:
            break

    print("\nPosición inicial:", start)

    puntos_totales = 0

    while True:
        print("\nPuntos acumulados:", puntos_totales)
        print(campo)

        fila = int(input("Fila destino (-1 para salir): "))
        col = int(input("Columna destino (-1 para salir): "))

        if fila == -1 and col == -1:
            break

        puntos, campo = avance(campo, start, (fila, col))
        puntos_totales += puntos
        start = (fila, col)

    print("\nJuego terminado. Puntos finales:", puntos_totales)
    print("Tablero final:")
    print(campo)
