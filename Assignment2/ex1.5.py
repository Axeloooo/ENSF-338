# Importing timeit to measure the time of the functions
import timeit
# Importing matplotlib to plot the results
import matplotlib.pyplot as plt

# Function to calculate the nth fibonacci number without memoization


def nomemofib(n):
    if n == 0 or n == 1:
        return n
    else:
        return nomemofib(n-1) + nomemofib(n-2)

# Function to calculate the nth fibonacci number with memoization


def memofib(n, memo={}):
    if n == 0 or n == 1:
        return n
    elif n in memo:
        return memo[n]
    else:
        memo[n] = memofib(n - 1, memo) + memofib(n - 2, memo)
        return memo[n]


# Lists to store the times of the functions
nomemofib_times = []
memofib_times = []

# Loop to calculate the times of the functions
for n in range(36):
    nomemofib_times.append(timeit.timeit(lambda: nomemofib(n), number=1))
    memofib_times.append(timeit.timeit(lambda: memofib(n), number=1))

# Plotting the results
plt.scatter(range(36), nomemofib_times, label='nomemofib')
plt.scatter(range(36), memofib_times, label='memofib')
plt.xlabel('n')
plt.ylabel('time')
plt.legend()
plt.show()
