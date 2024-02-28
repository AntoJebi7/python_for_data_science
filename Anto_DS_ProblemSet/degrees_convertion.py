import numpy as np
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
# Array of temperatures in Celsius
celsius_temperatures = np.array([0, 10, 20, 30, 40])
# Convert Celsius to Fahrenheit
fahrenheit_temperatures = celsius_to_fahrenheit(celsius_temperatures)
print("Temperatures in Fahrenheit:", fahrenheit_temperatures)
# Array of temperatures in Fahrenheit
fahrenheit_temperatures = np.array([32, 50, 68, 86, 104])
# Convert Fahrenheit to Celsius
celsius_temperatures = fahrenheit_to_celsius(fahrenheit_temperatures)
print("Temperatures in Celsius:", celsius_temperatures)


'''
Temperatures in Fahrenheit: [32.  50.  68.  86. 104.]
Temperatures in Celsius: [ 0. 10. 20. 30. 40.]

'''