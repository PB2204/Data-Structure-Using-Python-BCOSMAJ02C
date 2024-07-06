# Function to convert a dense matrix to a sparse matrix
def dense_to_sparse(matrix):
    sparse_matrix = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse_matrix.append((i, j, matrix[i][j]))
    return sparse_matrix

# Function to convert a sparse matrix back to a dense matrix
def sparse_to_dense(sparse_matrix, rows, cols):
    dense_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for row, col, value in sparse_matrix:
        dense_matrix[row][col] = value
    return dense_matrix

# Define a 6x6 dense matrix
A = [
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0],
    [1, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 3, 0],
    [0, 1, 0, 0, 0, 3]
]

print("\nDense Matrix:")
for row in A:
    print(row)

# Convert the dense matrix to a sparse matrix
sparse_matrix = dense_to_sparse(A)
print("\nSparse Matrix:", sparse_matrix)

# Convert the sparse matrix back to a dense matrix
# rows, cols = 6, 6
rows = len(A)
cols = len(A[0])

reconstructed_dense_matrix = sparse_to_dense(sparse_matrix, rows, cols)
print("\nReconstructed Dense Matrix:")
for row in reconstructed_dense_matrix:
    print(row)
