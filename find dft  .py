import numpy as np
import matplotlib.pyplot as plt
import time

def create_twiddle_matrix(size):
    # Indented the code block within the function definition
    twiddle_matrix = np.zeros((size, size), dtype=complex)
    for row in range(size):
        for col in range(size):
            twiddle_matrix[row, col] = np.exp(-2j * np.pi * row * col / size)
    return twiddle_matrix

order = int(input("Enter the order of the twiddle factor: "))
twiddle_matrix = create_twiddle_matrix(order)
print("Generated Twiddle Factor Matrix:")
print(twiddle_matrix)
real_component = np.random.rand(order, 1)
imag_component = np.random.rand(order, 1)
signal = real_component + 1j * imag_component
print("Input Signal (X[n]):")
print(signal)
dft_result = np.dot(twiddle_matrix, signal)
print("DFT Result Matrix:")
print(dft_result)
