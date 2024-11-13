import numpy as np
import matplotlib.pyplot as plt

sampling_freq = 100
time_points = np.linspace(0, 1, sampling_freq)
composite_signal = (
    np.cos(2 * np.pi * 1 * time_points) +
    0.5 * np.cos(2 * np.pi * 4 * time_points) +
    2 * np.cos(2 * np.pi * 7 * time_points)
)

plt.figure(figsize=(10, 5))
# Time-Domain Representation
plt.subplot(2, 1, 1)
plt.plot(time_points, composite_signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Time-Domain Representation")

# Frequency Spectrum (FFT)
fft_values = np.fft.fft(composite_signal, sampling_freq)
freq_bins = np.fft.fftfreq(len(fft_values), 1 / sampling_freq)

# Plot Frequency Spectrum
plt.subplot(2, 1, 2)
plt.stem(freq_bins[:len(freq_bins)//2], np.abs(fft_values[:len(freq_bins)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')  # Corrected the title
plt.grid(True)
plt.tight_layout()
plt.show()
