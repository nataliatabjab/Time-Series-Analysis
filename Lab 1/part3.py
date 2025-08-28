import math
import numpy as np
import matplotlib.pyplot as plt

# Helper function to make the Gaussian Functions
def gaussian(t, t_H):
    return (1 / (np.sqrt(np.pi) * t_H)) * np.exp(-(t / t_H)**2)

# Data file
file_path = "RAYN.II.LHZ.sem"
time, displacement = np.loadtxt(file_path, unpack=True)

dt = 0.1615 # Sampling Interval
start_index = 8 # Index at which time is approximately 0
limit_index = math.ceil(800/dt) # Index at which time = 800s approx

# Data in between 0 and 800 seconds
time_range = time[start_index:limit_index]
displacement_range = displacement[start_index:limit_index]

# Convolving Raw Data with Gaussians
convolved_10 = np.convolve(displacement_range, gaussian(time_range, 10))[:len(displacement_range)]
convolved_20 = np.convolve(displacement_range, gaussian(time_range, 20))[:len(displacement_range)]

# Sampling range for Gaussians
sample_ten = np.arange(-30, 30, dt)
sample_twenty = np.arange(-60, 60, dt)

# Plot 1: Gaussian functions with Half Durations of 10s and 20s 
plt.plot(sample_ten, gaussian(sample_ten, 10), label = "Gaussian with Half Duration of 10s")
plt.plot(sample_twenty, gaussian(sample_twenty, 20), label = "Gaussian with Half Duration of 20s")
plt.title("Gaussian Functions with Half Durations of 10s and 20s")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.figure()


# Plot 2: Raw synthetic seismogram for station RAYN between 0 and 800 seconds 
plt.plot(time_range, displacement_range, label = "Raw synthetic seismogram data") # Raw data
plt.plot(time_range, convolved_10, label = "Convolved Data: Half Dur. 10s") # Convolved data)
plt.title("Raw synthetic seismogram for station RAYN")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
# plt.figure()

# # plt.plot(time_range, displacement_range, label = "Raw synthetic seismogram data") # Raw data
plt.plot(time_range, convolved_20, label = "Convolved Data: Half Dur. 20s") # Convolved data)
# plt.title("Raw synthetic seismogram for station RAYN")
# plt.xlabel("Time (s)")
# plt.ylabel("Displacement (m)")
# plt.legend()
plt.show()