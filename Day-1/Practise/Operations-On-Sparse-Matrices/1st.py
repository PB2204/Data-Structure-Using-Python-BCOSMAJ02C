# Write a Python function to add two sparse matrices (represented as dictionaries of keys).

def add_sparse_matrices(matrix1, matrix2):
    result = {}
    for key in matrix1:
        if key in matrix2:
            result[key] = matrix1[key] + matrix2[key]
        else:
            result[key] = matrix1[key]
    for key in matrix2:
        if key not in matrix1:
            result[key] = matrix2[key]
    return result

# Example Usage

matrix1 = {
    (0, 0): 1,
    (1, 2): 2
}

matrix2 = {
    (0, 0): 3,
    (1, 2): 4
}

result = add_sparse_matrices(matrix1, matrix2)
print(result)

# Output
# {(0, 0): 4, (1, 2): 6}