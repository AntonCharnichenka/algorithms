from typing import Sequence

def get_max_elem(arr: Sequence[int]) -> int:
    """O(n)"""
    max = None
    for el in arr:
        if max is None:
            max = el
            continue

        if el > max:
            max = el
    
    return max


def get_max_elem_fast(arr: Sequence[int]) -> int:
    """O(1)"""
    ...


assert(get_max_elem([3, 10, 1, -5, 7]) ==10)
