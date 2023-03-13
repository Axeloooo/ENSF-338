# Assignment 3, Exercise 3.5 b

# Contributors: Axel Sanchez, Mariia Podgaietska

import heapq
import random
import timeit
from matplotlib import pyplot as plt


class inefficient_Queue:
    def __init__(self):
        self._queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self._queue])

    def isEmpty(self):
        return len(self._queue) == 0

    def queue(self, data):
        self._queue.append(data)

    def dequeue(self):
        try:
            max = 0
            for i in range(len(self._queue)):
                if self._queue[i] > self._queue[max]:
                    max = i
            item = self._queue[max]
            del self._queue[max]
            return item
        except IndexError:
            print()
            exit()


class efficient_Queue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def __str__(self):
        return ' '.join([str(i) for i in self._queue])

    def queue(self, priority, item):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0


# Generating random data and creating lists for storing the results
data = [random.randint(0, 1000) for i in range(1000)]
efficient_times_queueing = []
inefficient_times_queueing = []
efficient_times_dequeueing = []
inefficient_times_dequeueing = []
efficient_queue = efficient_Queue()
inefficient_queue = inefficient_Queue()


# Measuring the time it takes to queue for a value in the data
for i in range(1000):
    efficient_times_queueing.append(timeit.timeit(
        lambda: efficient_queue.queue(data[i], f'item {i}'), number=1))
    inefficient_times_queueing.append(timeit.timeit(
        lambda: inefficient_queue.queue(data[i]), number=1))


# Measuring the time it takes to dequeue for a value in the data
for i in range(1000):
    efficient_times_dequeueing.append(timeit.timeit(
        lambda: efficient_queue.dequeue(), number=1))
    inefficient_times_dequeueing.append(timeit.timeit(
        lambda: inefficient_queue.dequeue(), number=1))


# Print an aggregate of the target values
average = sum(data) / len(data)
print("Average target value: ", average)
print("Minimum target value: ", min(data))


# Plotting the results
plt.scatter(data, efficient_times_queueing,
            label='efficient queueing')
plt.scatter(data, inefficient_times_queueing,
            label='inefficient queueing')
plt.xlabel('target value')
plt.ylabel('time')
plt.legend()
plt.show()
plt.scatter(data, efficient_times_dequeueing,
            label='efficient dequeueing')
plt.scatter(data, inefficient_times_dequeueing,
            label='inefficient dequeueing')
plt.xlabel('target value')
plt.ylabel('time')
plt.legend()
plt.show()
