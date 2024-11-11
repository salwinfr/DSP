from numpy import *
from matplotlib.pyplot import *
def dft_matrix(N):
    n = arange(N)
    k = n[:, None]

    omega = exp(-2j*k*pi*n/N)
    print(omega)
    return omega
N = int(input("Enter the value: "))
dft = dft_matrix(N)
figure(figsize=(12,6))
subplot(1,2,1)
title(f"real values of DFT with N={N}")
imshow(real(dft))
colorbar()
subplot(1,2,2)
title(f"imaginary values of DFT with N={N}")
imshow(imag(dft))
colorbar()
show()