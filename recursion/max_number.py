def find_max_number(arr: list[int]) -> int:
    """Finds maximum number in the given array"""
    if len(arr) == 0:
        return 0
    
    return max(arr[0], find_max_number(arr[1:]))


assert find_max_number([1, 10, 30]) == 30
assert find_max_number([12, -12, 1]) == 12
assert find_max_number([]) == 0
