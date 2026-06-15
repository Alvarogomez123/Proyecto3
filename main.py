laberinto = [
    [1,  1,  1,  1,  0,  1,  1,  1,  1],
    [-2, 0,  0, -1,  0,  1,  0,  1,  0],
    [1,  1,  0,  1,  1,  1,  0,  1,  0],
    [0,  1,  0, -1,  0,  0,  0, -1,  0],
    [1,  1,  1,  1,  1,  1,  1,  1,  0],
    [-1, 0,  0,  0,  0,  0,  0,  1,  1],
    [1,  1,  1,  1, -1,  1,  1,  1,  0],
    [1,  0,  0,  1,  0,  1,  0,  1,  0],
    [1,  1, -1,  1,  1,  1,  0,  1,  1]
]

N = 9

inicio = (8, 0)
fin = (0, 0)

vidas_iniciales = 3

solucion = [[0] * N for _ in range(N)]

# Abajo, derecha, arriba, izquierda
movimientos = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def es_valido(fila, columna, visitado):
    return (
        0 <= fila < N and
        0 <= columna < N and
        laberinto[fila][columna] != 0 and
        not visitado[fila][columna]
    )


def backtracking(fila, columna, vidas, visitado):
    print(f"Ratón en ({fila},{columna}) - Vidas: {vidas}")

    if (fila, columna) == fin:
        solucion[fila][columna] = 1
        return True

    visitado[fila][columna] = True
    solucion[fila][columna] = 1

    for df, dc in movimientos:
        nf = fila + df
        nc = columna + dc

        if es_valido(nf, nc, visitado):

            nuevas_vidas = vidas

            if laberinto[nf][nc] == -1:
                nuevas_vidas -= 1
            elif laberinto[nf][nc] == -2:
                nuevas_vidas -= 2

            if nuevas_vidas >= 1:
                if backtracking(nf, nc, nuevas_vidas, visitado):
                    return True

    solucion[fila][columna] = 0
    visitado[fila][columna] = False

    return False


print("LABERINTO ORIGINAL")

for fila in laberinto:
    print(fila)

visitado = [[False] * N for _ in range(N)]

print("\nRECORRIDO DEL RATÓN")

if backtracking(inicio[0], inicio[1], vidas_iniciales, visitado):

    print("\n¡EL RATÓN LOGRÓ SALIR!")

    print("\nMATRIZ SOLUCIÓN:")

    for fila in solucion:
        print(fila)

else:
    print("\nNO EXISTE UN CAMINO VIABLE.")