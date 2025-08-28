import timeit
import numpy as np
import matplotlib.pyplot as plt

import numpy as np

def myConv(f, w):
    # Get the lengths of arrays f and w
    len_f, len_w = len(f), len(w)

    # Initialize the result array with zeros
    result = [0] * (len_f + len_w - 1)

    # Iterate over elements in f
    for i in range(len_f):
        # Iterate over elements in w
        for j in range(len_w):
            # Update the result array at the correct index
            result[i + j] += f[i] * w[j]

    return result

def arrayBuilder(n):
    return list(range(n))

sizes = [10, 100, 1000, 10000]
time_myConv = []
time_numpyConv = []

for n in sizes:
    f = arrayBuilder(n)
    w = arrayBuilder(n)

    time_myConv.append(timeit.timeit(lambda: myConv(f, w), number=10000))
    time_numpyConv.append(timeit.timeit(lambda: np.convolve(f, w), number=10000))

print(time_myConv, time_numpyConv)

plt.plot(sizes, time_myConv, label='myConv')
plt.plot(sizes, time_numpyConv, label='numpy Convolve')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Comparison of Convolution Functions')
plt.show()
