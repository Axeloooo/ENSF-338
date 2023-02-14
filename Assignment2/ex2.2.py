import sys
import json # import json module to read json file 'test'
import timeit  # import timeit module to measure execution time
import matplotlib.pyplot as plt # import matplotlib to plot the results

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# opening json file
with open("ex2_data.json", "r") as file:
    content = json.load(file)
    
times = []  # list to store times of execution
num_array_elements = [] # list to store number of elements in each array of test file

# loop to calculate time execution of functions with different input sizes
for n in range(len(content)):
    times.append(timeit.timeit(lambda: func1(content[n], 0, len(content[n]) - 1), number=1))
    num_array_elements.append(len(content[n]))  # store number of elements in each array of test file in list

# plot the results
plt.plot(num_array_elements, times)
plt.xlabel('num of elements in array')
plt.ylabel('sort execution time in seconds')
plt.show()