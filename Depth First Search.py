graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
found = []
x = input("Enter element for search:")


def dfs(visited, graph, node, x):
    if node not in visited:
        if x == node:
            found.append(x)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, x)


dfs(visited, graph, 'A', x)
if not found:
    print("Element not found")
else:
    print(found)
    print("Element found")
