# Function to calculate the nth fibonacci number with memoization


def memofib(n, memo={}):

    # If n is 0 or 1, return n
    if n == 0 or n == 1:
        return n

    # If n is in the memo, return the value of n
    elif n in memo:
        return memo[n]

    # Else, calculate the value of n and return it
    else:
        memo[n] = memofib(n - 1, memo) + memofib(n - 2, memo)
        return memo[n]
