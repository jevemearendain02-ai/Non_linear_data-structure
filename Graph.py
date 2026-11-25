
from collections import deque


def build_graph():
    graph = {
        "A1": [],
        "R": [],
        "E": [],
        "N1": [],
        "D": [],
        "A2": [],
        "I": [],
        "N2": []
    }

    edges = [
        ("A1", "R"),
        ("A1", "E"),
        ("R", "N1"),
        ("R", "D"),
        ("E", "A2"),
        ("E", "I"),
        ("N1", "N2"),
        ("D", "I"),
        ("A2", "N2")
    ]

    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    return graph


def bfs(graph, start):
    """Visit all reachable vertices level by level."""
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs(graph, start, visited=None, result=None):
    """Explore one path as deeply as possible before backtracking."""
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result


def main():
    graph = build_graph()

    print("================================")
    print(" GRAPH - ARENDAIN")
    print("================================")

    print("\nGraph connections (adjacency list):")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {', '.join(neighbors)}")

    print("\nBreadth-First Search (BFS), starting at A1:")
    print(" -> ".join(bfs(graph, "A1")))

    print("\nDepth-First Search (DFS), starting at A1:")
    print(" -> ".join(dfs(graph, "A1")))


if __name__ == "__main__":
    main()
