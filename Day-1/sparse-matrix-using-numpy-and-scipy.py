import numpy as np
from scipy.sparse import csr_matrix

# the array has to be of 3 x 7
A = np.array([[1, 0, 0, 1, 0, 0, 0],
              [0, 0, 2, 0, 0, 1, 0],
              [0, 0, 0, 2, 0, 0, 0]])

print("Row height is",len(A))
print("Column height is",len(A[0]))

print("Dense Matrix: \n", A)

# convert the array to a sparse matrix
B = csr_matrix(A)
print("Sparse Matrix: \n", B)

# convert the sparse matrix back to a dense matrix
C = B.todense()
print("Re Build Dense Matrix: \n", C)


