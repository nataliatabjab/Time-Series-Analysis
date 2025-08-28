import numpy as np
import matplotlib.pyplot as plt

# Define the discrete signal
g = np.array([1, 2, 3, 4, 5])

# Number of samples
N = len(g)

# Sampling interval
dt = 1

# Calculate Fourier Series Transform (FS)
G_fs = np.fft.fft(g) / N

# Calculate Inverse Fourier Series Transform (IFS)
g_ifs = np.fft.ifft(G_fs) * N

# Calculate Discrete Fourier Transform (DFT)
G_dft = np.fft.fft(g) * dt

# Display the results
plt.plot()