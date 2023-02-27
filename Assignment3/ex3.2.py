# Assignment 3, Exercise 3.2

# Contributors: Axel Sanchez, Mariya Podgaietska

import json
import random
import timeit
from matplotlib import pyplot as plt

# function to get the data


def get_data():
    with open("Assignment3/ex2tasks.json", "r") as json_file:
        return json.load(json_file)

# function to get the tasks


def get_tasks():
    with open("Assignment3/ex2tasks.json", "r") as json_file:
        return json.load(json_file)

# function to test the location of the target


def test_location(data, target, mid):
    mid_number = data[mid]
    if mid_number == target:
        if mid-1 >= 0 and data[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif mid_number < target:
        return 'left'
    else:
        return 'right'

# function to calculate the binary search


def binary_search(data, target, config=None):
    low = 0
    high = len(data) - 1

    while low <= high:

        if config is None:
            mid = (low + high) // 2
        else:
            mid = config
        result = test_location(data, target, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
            config = None
        elif result == 'right':
            low = mid + 1
            config = None

    return -1


# get the data and tasks
data = get_data()
tasks = get_tasks()


# lists to store the times of the functions
search_times = []
config_midpoints = []


# loop to calculate the times of the functions
for index in range(len(tasks)):
    config = random.randint(0, len(data)-1)
    config_midpoints.append(config)
    search_times.append(timeit.timeit(
        lambda: binary_search(data, tasks[index], config), number=1))


# Plotting the results
plt.scatter(config_midpoints, search_times, label='binary search')
plt.xlabel('configured midpoint')
plt.ylabel('time')
plt.legend()
plt.show()
