#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for i in range(len(matrix)):
        row = map(lambda x: x * x, matrix[i])
        matrix1.append(list(row))

    return matrix1
