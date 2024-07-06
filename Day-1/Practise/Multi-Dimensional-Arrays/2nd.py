# Implement a Python function to transpose a given 2D array.

def transpose(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transpose(arr))