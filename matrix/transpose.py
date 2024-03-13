def transpose(matrix):
    # Obtenemos el número de filas y columnas de la matriz original
    num_filas = len(matrix)
    num_columnas = len(matrix[0])  # Se asume que la matriz tiene al menos una fila

    # Creamos una matriz transpuesta vacía
    transpuesta = [[0] * num_filas for _ in range(num_columnas)]

    # Llenamos la matriz transpuesta intercambiando filas por columnas
    for i in range(num_filas):
        for j in range(num_columnas):
            transpuesta[j][i] = matrix[i][j]

    return transpuesta