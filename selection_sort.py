from typing import Sequence

def find_smallest(array: Sequence[int]) -> int:
    smallest_index = 0
    smallest = array[smallest_index]

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    
    return smallest_index


def selection_sort(array: Sequence[int]) -> list[int]:
    """O(n^2)"""
    sorted_array: list[int] = []
    for _ in range(len(array)):
        smallest_index = find_smallest(array)
        sorted_array.append(array.pop(smallest_index))
    
    return sorted_array



assert selection_sort([5, 3, 7, 1, 8, 9]) == [1, 3, 5, 7, 8, 9]
