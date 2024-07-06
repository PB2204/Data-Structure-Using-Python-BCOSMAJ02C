# Implement a Python function to reverse a single-dimensional array in place.

def reverse_array(array):
    length = len(array)
    for i in range(length // 2):
        array[i], array[length - i - 1] = array[length - i - 1], array[i]
    return array

# Example Usage:
Array = [1, 17, 14, 15, 16, 17, 25, 26, 76, 103, 55, 107, 83, 99]
print("Reversed Array Is: ", reverse_array(Array))