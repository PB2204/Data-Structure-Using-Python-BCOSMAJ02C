# Write a Python function to convert a dense 3x3 matrix to a sparse matrix using the list of tuples representation.

def dense_to_sparse(matrix):
    sparse_matrix = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse_matrix.append((i, j, matrix[i][j]))
    return sparse_matrix

# Example Usage

dense_matrix = [
    [1, 0, 0],
    [0, 0, 2],
    [0, 0, 0]
]

sparse_matrix = dense_to_sparse(dense_matrix)
print("Sparse Matrix (List of Tuples):", sparse_matrix)