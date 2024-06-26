def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    smaller: list[int] = [el for el in arr if e < pivot]
    greater: list[int] = [el for el in arr if e > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

    assert [10, 3, -3, 5, 1] == [-3, 1, 3, 5, 10]
    