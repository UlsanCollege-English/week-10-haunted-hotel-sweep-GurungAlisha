"""Week 10 Coding #8: Haunted Hotel Sweep."""

from collections import deque


Graph = dict[str, list[str]]


def get_neighbors(graph: Graph, area: str) -> list[str]:
    """Return neighboring areas, or [] if the area is missing.

    Example:
        >>> hotel = {"Lobby": ["Hallway"], "Hallway": ["Lobby"]}
        >>> get_neighbors(hotel, "Lobby")
        ['Hallway']
        >>> get_neighbors(hotel, "Tower")
        []
    """
    return graph.get(area, [])


def has_path(graph: Graph, start: str, target: str) -> bool:
    """Return True if target is reachable from start.

    Return False if either area is missing or if target cannot be reached.
    If start == target and the area exists, return True.
    """
    if start not in graph or target not in graph:
        return False

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == target:
            return True
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return False


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return areas in breadth-first sweep order.

    Use a queue with collections.deque.
    Use the neighbor order exactly as given in the graph.
    Return [] if start is missing.
    """
    if start not in graph:
        return []

    visited = set()
    queue = deque([start])
    order = []

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        order.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return order


def dfs_order(graph: Graph, start: str) -> list[str]:
    """Return areas in depth-first sweep order.

    Use a stack.
    Use the neighbor order exactly as given in the graph.
    Return [] if start is missing.
    """
    if start not in graph:
        return []

    visited = set()
    stack = [start]
    order = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        order.append(current)
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


def count_reachable_areas(graph: Graph, start: str) -> int:
    """Return how many unique areas are reachable from start.

    Stretch function. Return 0 if start is missing.
    """
    if start not in graph:
        return 0
    return len(bfs_order(graph, start))


if __name__ == "__main__":
    hotel = {
        "Lobby":    ["Hallway", "Ballroom"],
        "Hallway":  ["Lobby", "Room 13"],
        "Ballroom": ["Lobby"],
        "Room 13":  ["Hallway", "Attic"],
        "Attic":    ["Room 13"],
        "Cellar":   [],
    }

    print("BFS from Lobby :", bfs_order(hotel, "Lobby"))
    print("DFS from Lobby :", dfs_order(hotel, "Lobby"))
    print("Has path Lobby -> Attic :", has_path(hotel, "Lobby", "Attic"))
    print("Has path Lobby -> Cellar:", has_path(hotel, "Lobby", "Cellar"))
    print("Reachable from Lobby    :", count_reachable_areas(hotel, "Lobby"))
    print("Neighbors of Lobby      :", get_neighbors(hotel, "Lobby"))
    print("Neighbors of Tower      :", get_neighbors(hotel, "Tower"))