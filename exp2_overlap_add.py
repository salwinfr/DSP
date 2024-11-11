import numpy as np 
from scipy.fft import fft, ifft 
def overlap_add(x, h):
   N = len(x)   
   M = len(h)  
   L = N // 4  
   P = M + L - 1   
   H = fft(h, P)   
   y = np.zeros(N + M - 1) 
   for i in range(0, N, L): 
        x_segment = x[i:i+L]  
        x_segment = np.pad(x_segment, (0, P - len(x_segment)), mode='constant')   
        Y_segment = ifft(fft(x_segment) * H).real
        y[i:i+P] += Y_segment 
   return y 
x = [1,2,3,4,5,6,7]
h = [1,1,1]
y_overlap_add = overlap_add(x, h) 
print("Output length:", len(y_overlap_add)) 
print("First few values of output:", y_overlap_add[:10])