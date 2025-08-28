import numpy as np
import matplotlib.pyplot as plt
import timeit

def myConv(f, w):
    len_f, len_w = len(f), len(w)
    result = [0] * (len_f + len_w - 1)

    for i in range(len_f):
        for j in range(len_w):
            result[i + j] += f[i] * w[j]

    return result

# Testing myConv
import random
arr1 = []
arr2 = []

arr1 = np.random.rand(50)
arr2 = np.random.rand(100)

g = np.convolve(arr1, arr2)
result = myConv(arr1, arr2)
plt.plot(g-result)

print("Result from myConv:", result)
print("Result from numpy convolve:", g)


def arrayBuilder(n):
    return list(range(n))

sizes = [10, 100, 1000]
time_myConv = []
time_numpyConv = []

for n in sizes:
    f = arrayBuilder(n)
    w = arrayBuilder(n)

    time_myConv.append(timeit.timeit(lambda: myConv(f, w), number=10000))
    print("Hello World")
    time_numpyConv.append(timeit.timeit(lambda: np.convolve(f, w), number=10000))

plt.plot(sizes, time_myConv, label='myConv')
plt.plot(sizes, time_numpyConv, label='numpy Convolve')
plt.title('Comparison of Convolution Functions')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.savefig('comparison_plot.png')