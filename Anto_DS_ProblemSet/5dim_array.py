import numpy as np

# Create a 5-dimensional array
array_5d = np.ndarray(shape=(2, 3, 4, 5, 6))

# Verify the dimensionality
if array_5d.ndim == 5:
    print("The array is 5-dimensional.")
else:
    print("The array is not 5-dimensional.")


