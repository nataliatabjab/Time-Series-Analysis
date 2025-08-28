import numpy as np


f_0 = 5
f_s = 5
z = 1 + 1j

def calc_numerator():
    return (z - np.exp(-1j*2*np.pi*(f_0/f_s))) * (z - np.exp(1j*2*np.pi*(f_0/f_s)))

print(calc_numerator())