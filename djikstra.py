import copy

GRAPH = {}

GRAPH['start'] = {}
GRAPH['start']['a'] = 6
GRAPH['start']['b'] = 2
GRAPH['a'] = {}
GRAPH['a']['fin'] = 1
GRAPH['b'] = {}
GRAPH['b']['a'] = 3
GRAPH['b']['fin'] = 5
GRAPH['fin'] = {}

COSTS = {}
COSTS['a'] = 6
COSTS['b'] = 2
COSTS['fin'] = float('inf')

PARENTS = {}
PARENTS['a'] = 'start'
PARENTS['b'] = 'start'
PARENTS['fin'] = None

def search(graph, costs, parents) -> str:
    processed: set[str] = set()

    node = min(costs, key=lambda node: costs[node])
    while node:
        cost = costs[node]
        neighbour_nodes = graph[node]

        for neighbour_node in neighbour_nodes:
            new_cost = cost + neighbour_nodes[neighbour_node]

            if costs[neighbour_node] > new_cost:
                costs[neighbour_node] = new_cost
                parents[neighbour_node] = node

        processed.add(node)
        if (pool := set(costs) - processed):
            node = min(pool, key=lambda node: costs[node])
        else:
            node = None
    
    path: list[str] = ['fin']
    node = parents['fin']
    while node != 'start':
        path.append(node)
        node = parents[node]
    path.append('start')
    
    return ' -> '.join(reversed(path))


assert search(GRAPH, COSTS, PARENTS) == 'start -> b -> a -> fin'


GRAPTH2 = copy.deepcopy(GRAPH)
GRAPTH2['b']['fin'] = 1

assert search(GRAPTH2, COSTS, PARENTS) == 'start -> b -> fin'
