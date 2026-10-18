from collections import defaultdict
from typing import Callable

# Build the method to calculate the Fibonacci number.
def caching_fibonacci() -> Callable[[int], int]:
    # Initialize cache as a dict with a default value of 0.
    cache = defaultdict(int)

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1

        # Return the cached result if it exists.
        if n in cache:
            return cache[n]

        # Calculate the Fibonacci number and add it to cache.
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
