import numpy as np
from scipy.fft import fft, ifft

def overlap_save(x, h):
    N = len(x)
    M = len(h)
    L = N // 2
    P = M + L - 1

    H = fft(h, P)
    y = np.zeros(N)
    x_padded = np.pad(x, (M - 1, 0), mode='constant')

    for i in range(0, len(x), L):
        x_segment = x_padded[i : i + P]
        if len(x_segment) < P:
            x_segment = np.pad(x_segment, (0, P - len(x_segment)), mode='constant')
        Y_segment = ifft(fft(x_segment) * H).real
        seg_len = min(L, len(y) - i)
        y[i : i + seg_len] = Y_segment[M - 1 : M - 1 + seg_len]
    return y

# Test the function
x = [1, 2, 3, 4, 5, 6, 7]
h = [1, 1, 1]
y_overlap_save = overlap_save(x, h)
print("Output length:", len(y_overlap_save))
print("First few values of output:", y_overlap_save[:10])
