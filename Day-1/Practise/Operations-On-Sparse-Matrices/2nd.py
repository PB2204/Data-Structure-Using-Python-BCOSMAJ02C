# Implement a Python function to multiply two sparse matrices (represented as dictionaries of keys).

def multiply_sparse_matrices(matrix1, matrix2):
    result = {}
    for key1 in matrix1:
        for key2 in matrix2:
            if key1[1] == key2[0]:
                result[(key1[0], key2[1])] = result.get((key1[0], key2[1]), 0) + matrix1[key1] * matrix2[key2]
    return result

# Example Usage

matrix1 = {
    (0, 0): 1,
    (0, 1): 2,
    (1, 0): 3,
    (1, 1): 4
}

matrix2 = {
    (0, 0): 5,
    (0, 1): 6,
    (1, 0): 7,
    (1, 1): 8
}

result = multiply_sparse_matrices(matrix1, matrix2)
print(result)

# Output
# {(0, 0): 19, (0, 1): 22, (1, 0): 43, (1, 1): 50}