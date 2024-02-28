import numpy as np

# Create a numpy array
my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
# Transpose the array using .T attribute
transposed_array = my_array.T
# Transpose the array using numpy.transpose() function
# transposed_array = np.transpose(my_array)

print("Original Array:")
print(my_array)

print("\nTransposed Array:")
print(transposed_array)

'''
Original Array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Transposed Array:
[[1 4 7]
 [2 5 8]
 [3 6 9]]
'''