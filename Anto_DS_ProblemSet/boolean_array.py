import numpy as np

# Create a boolean array
boolean_array = np.array([True, False, True, True, False])

# Sort the boolean array
sorted_indices = np.argsort(boolean_array)

# Use the sorted indices to sort the boolean array
sorted_boolean_array = boolean_array[sorted_indices]

print("Original boolean array:", boolean_array)
print("Sorted boolean array:", sorted_boolean_array)

'''
Original boolean array: [ True False  True  True False]
Sorted boolean array: [False False  True  True  True]

'''