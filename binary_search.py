import math
from typing import Sequence


def binary_search(pool: Sequence[int], item: int) -> int | None:
    """O(logN)"""
    low = 0
    high = len(pool) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)

        guess = pool[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        
        if guess < item:
            low  = mid + 1

    return None


assert binary_search([1, 3, 5, 7 ,9], 3) == 1
assert binary_search([1, 3, 5, 7 ,9], -1) is None
