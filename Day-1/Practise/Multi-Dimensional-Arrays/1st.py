# Create a 2D array (matrix) and write a Python function to find the sum of all elements in the matrix.

# Create a 2D array (matrix) From the User Input

rows = int(input("Enter The Number Of Rows: "))
columns = int(input("Enter The Number Of Columns: "))
Matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter The Element At Position {i+1},{j+1}: "))
        row.append(element)
    Matrix.append(row)

# Python Function to find the sum of the all elements in the matrix

def sum_of_elements(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum

# Example Usage

print("The Sum Of All Elements In The Matrix Is: ", sum_of_elements(Matrix))