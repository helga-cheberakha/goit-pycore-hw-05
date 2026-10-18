import re
from typing import Callable, Generator

# Find all numbers in the text.
def generator_numbers(text: str) -> Generator:
    # Find all numbers in the text with or without a decimal point.
    # Yield each number as a float, one at a time.
    for match in re.finditer(r'\b\d+(?:\.\d+)?\b', text):
        yield float(match.group())

# Calculate the sum of all numbers in the text.
def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

text = "The employee's total income consists of several parts: a base salary of 1000.01, supplemented by additional payments of 27.45 and 324"
total_income = sum_profit(text, generator_numbers)
print(f'Total income: {total_income}')
