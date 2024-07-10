from collections import deque
from typing import Callable

GRAPH: dict[str, list[str]] = {}
GRAPH['me'] = ['alice', 'bob', 'claire']
GRAPH['alice'] = ['peggy']
GRAPH['bob'] = ['anuj', 'peggy']
GRAPH['claire'] = ['thom', 'jonny']
GRAPH['peggy'] = []
GRAPH['anuj'] = []
GRAPH['thom'] = []
GRAPH['jonny'] = []


def search(name: str, key: Callable[[str], bool]) -> str | None:
    queue = deque()
    queue += GRAPH[name]
    seen: set[str] = set()

    while queue:
        person = queue.popleft()
        if not person in seen:
            if key(person):
                print(f'Person is found: {person}')
                return person
            
            queue += GRAPH[person]
            seen.add(person)
    
    print(f'Person has not been found')
    return None

assert search('me', lambda person: person == 'jonny') == 'jonny'
assert search('me', lambda person: person == 'sunny') is None
