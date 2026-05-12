from collections import deque

Graph = dict[str, list[str]]


def get_neighbors(graph: Graph, area: str) -> list[str]:
    return graph.get(area, [])


def has_path(graph: Graph, start: str, target: str) -> bool:
    if start not in graph or target not in graph:
        return False

    if start == target:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == target:
            return True

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False


def bfs_order(graph: Graph, start: str) -> list[str]:
    if start not in graph:
        return []

    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs_order(graph: Graph, start: str) -> list[str]:
    if start not in graph:
        return []

    visited = set()
    order = []
    stack = [start]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            order.append(current)

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def count_reachable_areas(graph: Graph, start: str) -> int:
    if start not in graph:
        return 0

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(visited)