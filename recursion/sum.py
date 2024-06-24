def sum(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] + sum(arr[1:])


assert sum([1, 2, 3, 4, 5]) == 15
assert sum([-1, 3, 7, -4]) == 5
