from numpy import *
from scipy.signal import freqz
from matplotlib.pyplot import *
from scipy.signal.windows import hamming,kaiser
M = 100
n = 100 
sizen = arange(0, n)
wn = zeros(n)
wn[:M-1] = 1 
wc = 0.3 * pi
wn_hamming =hamming(M)
hdn1 = zeros(n)

def hd1(wc, n):
    for i in range(0, n-1):
        if i == 0:
            hdn1[i] = wc/pi
        else:
            hdn1[i] = sin(wc * i) / (pi * i)
    return hdn1

hdn = hd1(wc, n)
hn = hdn * wn_hamming

# Compute the frequency response
w, h = freqz(hn)
h=20*log10((h))
# # Plot the impulse response

plot(sizen, wn_hamming)
title('Hamming Response')
xlabel('Sample')
ylabel('Amplitude')
grid()

# Plot the magnitude response
figure()
plot(w / pi,h)
title('Frequency Response')
xlabel('Normalized Frequency (×π rad/sample)')
ylabel('Magnitude')
grid()
show()

print(hn)