import time
import numpy as np
import matplotlib.pyplot as plt

def dft_matrix_create(N):
    dft_matrix = np.zeros((N, N), dtype=complex)
    for x in range(N):
        for y in range(N):
            dft_matrix[x, y] = np.exp(-2j * np.pi * x * y / N)
    return dft_matrix

N = [4, 8, 16, 32, 64, 256, 512,1024]
computation_method = []
computation_automated = []
for i in N:
    print(i)
    vx = np.random.randn(i)
    start_time = time.time()
    a = dft_matrix_create(i)
    np.matmul(a, vx)
    end_time = time.time()
    computation_time_method = end_time - start_time
    start_fft_time = time.time()
    b = np.fft.fft(vx)
    end_fft_time = time.time()
    computation_time_automated = end_fft_time - start_fft_time
    computation_method.append(computation_time_method)
    computation_automated.append(computation_time_automated)

plt.plot(N, computation_method, label='Manual Fourier Transform')
plt.plot(N, computation_automated, label='Fast Fourier Transform')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid()
plt.show()
