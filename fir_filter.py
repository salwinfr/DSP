import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

# Define filter parameters
N = 200
omega_c = 0.15 * np.pi  # Convert to radians
M = 50
n = np.arange(-N, N)

# Ideal filter (sinc function)
h_ideal = np.sinc(omega_c / np.pi * n)  # normalized sinc function

# Plot ideal filter impulse response
plt.figure(1)
plt.plot(n, h_ideal)
plt.title("Ideal Impulse Response")
plt.xlabel("n")
plt.ylabel("h_ideal[n]")

# Rectangular window
rect_window = np.array([1 if np.abs(val) < M else 0 for val in n])
h_windowed_rect = h_ideal * rect_window

plt.figure(2)
plt.plot(n, rect_window)
plt.title("Rectangular Window")
plt.xlabel("n")
plt.ylabel("w[n]")

plt.figure(3)
plt.plot(n, h_windowed_rect)
plt.title("Windowed Impulse Response (Rectangular Window)")
plt.xlabel("n")
plt.ylabel("h[n]")

# Hamming window
hamm_window = np.hamming(2 * N)
h_windowed_hamm = h_ideal * hamm_window

plt.figure(4)
plt.plot(n, hamm_window)
plt.title("Hamming Window")
plt.xlabel("n")
plt.ylabel("w[n]")

plt.figure(5)
plt.plot(n, h_windowed_hamm)
plt.title("Windowed Impulse Response (Hamming Window)")
plt.xlabel("n")
plt.ylabel("h[n]")

# Hanning window
hann_window = np.hanning(2 * N)
h_windowed_hann = h_ideal * hann_window

plt.figure(6)
plt.plot(n, hann_window)
plt.title("Hanning Window")
plt.xlabel("n")
plt.ylabel("w[n]")

plt.figure(7)
plt.plot(n, h_windowed_hann)
plt.title("Windowed Impulse Response (Hanning Window)")
plt.xlabel("n")
plt.ylabel("h[n]")

# Frequency response
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Rectangular window frequency response
w, H_rect = sp.freqz(h_windowed_rect)
axs[0].plot(w / np.pi, 20 * np.log10(np.abs(H_rect)))
axs[0].set_title("Frequency Response (Rectangular Window)")
axs[0].set_xlabel("Normalized Frequency (×π rad/sample)")
axs[0].set_ylabel("Magnitude (dB)")
axs[0].grid()

# Hamming window frequency response
w, H_hamm = sp.freqz(h_windowed_hamm)
axs[1].plot(w / np.pi, 20 * np.log10(np.abs(H_hamm)))
axs[1].set_title("Frequency Response (Hamming Window)")
axs[1].set_xlabel("Normalized Frequency (×π rad/sample)")
axs[1].set_ylabel("Magnitude (dB)")
axs[1].grid()

# Hanning window frequency response
w, H_hann = sp.freqz(h_windowed_hann)
axs[2].plot(w / np.pi, 20 * np.log10(np.abs(H_hann)))
axs[2].set_title("Frequency Response (Hanning Window)")
axs[2].set_xlabel("Normalized Frequency (×π rad/sample)")
axs[2].set_ylabel("Magnitude (dB)")
axs[2].grid()

plt.tight_layout()
plt.show()
