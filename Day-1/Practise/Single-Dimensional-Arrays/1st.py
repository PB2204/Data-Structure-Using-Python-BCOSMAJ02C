# Write a Python function to find the largest element in a single-dimensional array.

def find_largest_element(array):
    length = len(array)
    largest = array[0]
    for i in range(length):
        if array[i] > largest:
            largest = array[i]
    return largest

# Example Usage
Array = [1, 17, 14, 15, 16, 17, 25, 26, 76, 103, 55, 107, 83, 99]
print("The Largest Number In the Array Is: ", find_largest_element(Array))