import numpy as np
import matplotlib.pyplot as plt

## QUESTION 1 

dt = 0.001

# Helper function to make the Gaussian Functions
def gaussian(t, t_H):
    return (1 / (np.sqrt(np.pi) * t_H)) * np.exp(-(t / t_H)**2)


# Sampling range for Gaussians
sample_range = np.arange(-100, 100, dt)


# Plot 1: Gaussian functions with Half Durations of 10s and 20s 
plt.plot(sample_range, gaussian(sample_range, 20), label = "Gaussian with Half Duration of 20s")
plt.plot(sample_range, gaussian(sample_range, 40), label = "Gaussian with Half Duration of 40s")
plt.title("Gaussian Functions with Half Durations of 20s and 40s")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.show()


## QUESTION 2

g_20 = gaussian(sample_range, 20)
g_40 = gaussian(sample_range, 40)

# Number of samples
N = len(g_20)

# Frequency axis for plotting
f_axis = np.fft.fftshift(np.fft.fftfreq(N, dt))

# Angular frequency axis for plotting
w_axis = 2 * np.pi * f_axis

# Analytical FT := G(w)
analytical_20 = np.exp(-((w_axis)**2)*(20**2)*0.25)
analytical_40 = np.exp(-((w_axis)**2)*(40**2)*0.25)

# Compute the FFT of the signals (applying the shift property)
dft_20 = np.fft.fftshift(np.fft.fft(g_20)) * dt
dft_40 = np.fft.fftshift(np.fft.fft(g_40)) * dt

# Generate complex exponential sinusoid function
sinusoid_20 = np.exp(1j * w_axis * 20)
sinusoid_40 = np.exp(1j * w_axis * 40)

# Correct the spectrum by multiplying with the sinusoid
corrected_spectrum_20 = dft_20 * sinusoid_20
corrected_spectrum_40 = dft_40 * sinusoid_40

plt.figure();
plt.title("Analytical Fourier Transforms of Gaussian Functions with Half Durations of 20s and 40s")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.plot(w_axis, analytical_20)
plt.plot(w_axis, analytical_40)

plt.figure();
plt.title("Actual DFTs of Gaussian Functions with Half Durations of 20s and 40s")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.plot(f_axis, np.abs(corrected_spectrum_20))
plt.plot(f_axis, np.abs(corrected_spectrum_40))
plt.show()