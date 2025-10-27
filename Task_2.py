from typing import Callable, Iterator
import re

def generator_numbers(text: str) -> Iterator[float]:
    """
    This generator extracts integer and decimal numbers from a text
    and yields each number as a float.
    """
    for match in re.findall(r'\d+(?:\.\d+)?', text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """
    This function uses the generator function to calculate the total sum
    of numbers in the input string.
    """
    total = 0.0
    for number in func(text):
        total += number
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, " \
"доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")