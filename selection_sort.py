from typing import Sequence

def find_smallest(arr: Sequence[int]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selection_sort(arr: Sequence[int]) -> list[int]:
    sorted_arr: list[int] = []
    for _ in range(len(arr)):
        smallest_index = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_index))
    
    return sorted_arr



assert selection_sort([5, 3, 7, 1, 8, 9]) == [1, 3, 5, 7, 8, 9]
