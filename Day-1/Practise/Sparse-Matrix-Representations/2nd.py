# Implement a Python function to convert a sparse matrix represented as a list of tuples back to a dense matrix.

def sparse_to_dense(sparse_matrix):
    rows = 0
    cols = 0
    for i in sparse_matrix:
        if i[0] > rows:
            rows = i[0]
        if i[1] > cols:
            cols = i[1]
    rows += 1
    cols += 1
    dense_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in sparse_matrix:
        dense_matrix[i[0]][i[1]] = i[2]
    return dense_matrix

# Example Usage

sparse_matrix = [
    (0, 0, 1),
    (1, 2, 2)
]

dense_matrix = sparse_to_dense(sparse_matrix)
for row in dense_matrix:
    print(row)