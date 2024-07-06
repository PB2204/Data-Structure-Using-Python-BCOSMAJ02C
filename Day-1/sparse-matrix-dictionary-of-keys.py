def dense_to_sparse(matrix):
    sparse_matrix = {}
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse_matrix[(i, j)] = matrix[i][j]
    return sparse_matrix

def sparse_to_dense(sparse_matrix, rows, cols):
    dense_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for (row, col), value in sparse_matrix.items():
        dense_matrix[row][col] = value
    return dense_matrix

# Example usage
dense_matrix = [
    [1, 0, 0],
    [0, 0, 2],
    [0, 0, 0]
]

sparse_matrix = dense_to_sparse(dense_matrix)
print("Sparse Matrix (Dictionary of Keys):", sparse_matrix)

reconstructed_dense_matrix = sparse_to_dense(sparse_matrix, 3, 3)
print("Reconstructed Dense Matrix:")
for row in reconstructed_dense_matrix:
    print(row)