import numpy as np

# Create an array of complex numbers
complex_array = np.array([1+2j, 3-4j, 5+6j])

# Find the real parts of the complex numbers
real_parts = np.real(complex_array)

# Find the imaginary parts of the complex numbers
imaginary_parts = np.imag(complex_array)

print("Complex array:", complex_array)
print("Real parts:", real_parts)
print("Imaginary parts:", imaginary_parts)


'''
Complex array: [1.+2.j 3.-4.j 5.+6.j]
Real parts: [1. 3. 5.]
Imaginary parts: [ 2. -4.  6.]
'''