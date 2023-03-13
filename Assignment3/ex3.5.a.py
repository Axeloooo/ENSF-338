# Assignment 3, Exercise 3.5 a

# Contributors: Axel Sanchez, Mariia Podgaietska


# Importing libraries
import random
import timeit
from matplotlib import pyplot as plt


# Function that searches for a target value in a list of numbers in a binary way


def efficient_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_number = data[mid]
        if mid_number == target:
            if mid-1 >= 0 and data[mid-1] == target:
                high = mid - 1
            else:
                return mid
        elif mid_number < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


# Function that searches for a target value in a list of numbers in a linear way


def inefficient_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return None


# Generating random data and creating lists for storing the results
data = list(range(1000))
efficient_search_times = []
inefficient_search_times = []
targets = []


# Measuring the time it takes to search for a target value in the data
for i in range(1000):
    target = random.randint(0, len(data)-1)
    targets.append(target)
    efficient_search_times.append(timeit.timeit(
        lambda: efficient_search(data, target), number=1))
    inefficient_search_times.append(timeit.timeit(
        lambda: inefficient_search(data, target), number=1))


# Print an aggregate of the target values
average = sum(targets) / len(targets)
print("Average target value: ", average)
print("Minimum target value: ", min(targets))


# Plotting the results
plt.scatter(targets, efficient_search_times, label='efficient search')
plt.scatter(targets, inefficient_search_times, label='inefficient search')
plt.xlabel('target value')
plt.ylabel('time')
plt.legend()
plt.show()
