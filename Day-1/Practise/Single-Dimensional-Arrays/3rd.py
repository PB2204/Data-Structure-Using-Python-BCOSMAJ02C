# Write a Python function to check if a given element exists in a single-dimensional array.

def check_element(array, element):
    length = len(array)
    for i in range(length):
        if array[i] == element:
            return True
    return False

# Example Usage

Array = [1, 17, 14, 15, 16, 17, 25, 26, 76, 103, 55, 107, 83, 99]
Element = 103
print("Lets Check: Element Exists In The Array Or Not: \n", check_element(Array, Element))
