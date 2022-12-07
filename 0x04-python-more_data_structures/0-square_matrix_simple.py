#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for i in range(len(matrix)):
        row = map(lambda x: x * x, matrix[i])
        matrix1.append(list(row))

    return matrix1

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
matrix1 = square_matrix_simple(matrix)
print(matrix1)
print(matrix)
