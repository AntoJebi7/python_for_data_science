import numpy as np
# Create two numpy arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
# Addition
addition_result = array1 + array2
print("Addition Result:")
print(addition_result)
# Subtraction
subtraction_result = array1 - array2
print("\nSubtraction Result:")
print(subtraction_result)
# Multiplication (element-wise)
multiplication_result = array1 * array2
print("\nMultiplication Result (element-wise):")
print(multiplication_result)
# Division (element-wise)
# Note: Be careful with division by zero
division_result = array1 / array2
print("\nDivision Result (element-wise):")
print(division_result)
# Matrix multiplication
matrix_multiplication_result = np.dot(array1, array2)
print("\nMatrix Multiplication Result:")
print(matrix_multiplication_result)
