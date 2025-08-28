import numpy as np;

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

g = np.convolve(arr1, arr2)



def myConv(arr1, arr2):
    # Initializing array in which to store convolution result
    result = []
    for i in range(0, len(arr1) + len(arr2) - 1):
        current_sum = 0
        # j will be used to iterate over the elements in arr1
        for j in range(len(arr1)):
            # k will be used to iterate over the elements in arr2
            for k in range(len(arr2)):
                if (j + k == i):
                    current_sum += arr1[j] * arr2[k]
        # Append the sum to the result array for the current index i
        result.append(current_sum)
    return result

            
result = myConv(arr1, arr2)
print(result, g)