def binary_search(arr: list[int], item: int) -> int | None:
    """Recursive implementation of binary search algoritm"""
    if len(arr) == 1:
        if arr[0] == item:
            return 0
        else:
            return None
    
    mid = int(len(arr) / 2)
    if arr[mid] > item:
        return binary_search(arr[:mid], item)
    else:
        try:
            return mid + binary_search(arr[mid:], item)
        except TypeError:
            return None


assert binary_search([1, 3, 7, 9, 10, 12], 7) == 2
assert binary_search([1, 3, 7, 9, 10, 12], -1) == None
assert binary_search([1, 3, 7, 9, 10, 12], 15) == None
