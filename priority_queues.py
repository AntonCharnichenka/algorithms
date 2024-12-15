import heapq

a = [3, 5, 1, 2, 6, 8, 7]
heapq.heapify(a)
# since every sorted list does satisfy the heap property, 
# running heapify() on a sorted list won’t change the order of elements in the list
print(a)


heapq.heappop(a)  # To pop the smallest element while preserving the heap property
print(a)


# HEAPS are concrete data structures - implementations for priority queues in python,
# which are abstract data structure

# HEAPS are good forfinding 'best' element, like min or max in O(1) time,
# because heaps are guarantee to follow heap property: h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]

# the time it takes to do push and pop is proportional to the base-2 logarithm of the number of elements.

# Also HEAPS are good for merging two sorted arrays

print('---')
import datetime
from typing import Generator

def email_gen(frequency: datetime.timedelta, text: str) -> Generator[tuple[datetime.datetime, str], None, None]:
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, text


frequent_email = email_gen(datetime.timedelta(minutes=15), 'fast_email')
less_frequent_email = email_gen(datetime.timedelta(minutes=45), 'slow_email')

unified = heapq.merge(frequent_email, less_frequent_email)

for _ in range(10):
    print(next(unified))


# EXAMPLE: finding paths (heapq + dynamic programming)
print('\n\n\n---EXAMPLE FIND PATH---')

import heapq
from typing import TypeAlias, Generator, Iterable

MAP = """\
.......X..
.......X..
....XXXX..
..........
..........
"""

Lines: TypeAlias = list[list[str]]
Position: TypeAlias = tuple[int, int]
PathLength: TypeAlias = int


def parse_map(map: str) -> tuple[Lines, Position, Position]:
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1

    return lines, origin, destination

def is_valid_position(lines: Lines, position: Position) -> bool:
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    
    if lines[y][x] == 'X':
        return False
    
    return True

def get_neighbors(lines: Lines, position: Position) -> Generator[Position, None, None]:
    x, y = position
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            maybe_valid_position = x + dx, y + dy
            if is_valid_position(lines, maybe_valid_position):
                yield maybe_valid_position

def maybe_get_shorter_paths_to_neighbors(
    shortest_paths: dict[Position, list[Position]], 
    neighbor_positions: Iterable[Position], 
    position: Position
) -> Generator[tuple[Position, list[Position]], None, None]:
    path = shortest_paths[position] + [position]
    for neigbor_position in neighbor_positions:
        if neigbor_position in shortest_paths and len(shortest_paths[neigbor_position]) <= len(path):
            continue
        
        yield neigbor_position, path


def find_path(map: str) -> list[Position]:
    lines, origin, destination = parse_map(map)

    # map of positions to the shortest known paths to that positions
    shortest_paths: dict[Position, list[Position]] = {origin: []}
    candidates: list[tuple[PathLength, Position]] = [(0, origin)]
    visited_positions: set[Position] = set()

    while destination not in visited_positions and len(candidates) > 0:
        _, current_position = heapq.heappop(candidates)
        if current_position in visited_positions:
            continue

        visited_positions.add(current_position)
        neighbors = set(get_neighbors(lines, current_position)) - visited_positions
        for neighbor, path in maybe_get_shorter_paths_to_neighbors(shortest_paths, neighbors, current_position):
            shortest_paths[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    
    if destination in shortest_paths:
        return shortest_paths[destination] + [destination]
    else:
        raise ValueError('No path found')


def show_path(map: str, path: list[Position]) -> None:
    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + '@' + lines[y][x+1:]
    
    return '\n'.join(lines) + '\n'


path = find_path(MAP)
print(show_path(MAP, path))
