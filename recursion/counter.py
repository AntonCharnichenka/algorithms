from typing import Any, Sequence

def count(arr: Sequence[Any]) -> int:
    """Counts number of elements in the given array"""
    if len(arr) == 0:
        return 0
    
    return 1 + count(arr[1:])

assert count([1, 2, 3]) == 3
assert count([]) == 0
