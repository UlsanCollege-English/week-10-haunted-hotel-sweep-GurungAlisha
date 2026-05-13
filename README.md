[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/I7NCKCh8)
# Week 10 Coding #8: Haunted Hotel Sweep

## Summary

This assignment models a haunted hotel as a graph where each area (Lobby, Hallway, Room 13, etc.) is a node and each connection between areas is an edge stored in an adjacency list. BFS (breadth-first search) explores the hotel level by level using a queue, visiting all neighbors of the current area before going deeper — useful for finding the shortest route. DFS (depth-first search) explores as far down one path as possible before backtracking, using a stack. The `visited` set is essential in both algorithms to prevent infinite loops when the graph contains cycles — without it, the traversal would bounce between connected areas forever and never terminate.

---

## Approach

- **Getting neighbors safely:** Used `graph.get(area, [])` so that if an area does not exist in the graph, an empty list is returned instead of raising a `KeyError`.
- **Checking whether a path exists:** Ran a BFS from `start`, returning `True` as soon as `target` is dequeued. Returned `False` early if either `start` or `target` is missing from the graph entirely.
- **BFS using a queue:** Initialized a `deque` with the start area. On each iteration, popped from the left, skipped if already visited, marked as visited, added to the result list, then appended all unvisited neighbors to the right of the queue.
- **DFS using a stack:** Initialized a plain list as a stack with the start area. On each iteration, popped from the end, skipped if already visited, marked as visited, added to the result list, then pushed neighbors in `reversed()` order so the first neighbor in the original list is explored first.
- **Preventing repeated visits:** Both BFS and DFS maintain a `visited` set. Before processing any area, the code checks membership in `visited` and skips it if already seen — this handles cycles and avoids duplicate entries in the result.
- **Counting reachable areas:** Reused `bfs_order` since it already returns every reachable area exactly once; the count is just the length of that list.

---

## Complexity

### `get_neighbors`

- Time: O(1)
- Space: O(1)
- Why: A single dictionary lookup with a default value — no iteration involved.

### `has_path`

- Time: O(V + E) where V is the number of areas and E is the number of connections
- Space: O(V) for the visited set and the queue
- Why: In the worst case, every area and every edge is examined once before the target is found or confirmed unreachable.

### `bfs_order`

- Time: O(V + E)
- Space: O(V) for the visited set and the queue
- Why: Each area is enqueued and dequeued at most once. Each edge is examined once when expanding neighbors.

### `dfs_order`

- Time: O(V + E)
- Space: O(V) for the visited set and the stack
- Why: Each area is pushed and popped at most once. Each edge is examined once when pushing neighbors.

### Stretch: `count_reachable_areas`

- Time: O(V + E)
- Space: O(V)
- Why: Delegates entirely to `bfs_order`, so it inherits the same complexity. The final `len()` call is O(1).

---

## Edge-Case Checklist

- [x] empty graph — `get_neighbors` returns `[]`; `has_path`, `bfs_order`, `dfs_order` all return early since the start key is not in the graph.
- [x] missing start area — all functions check `if start not in graph` and return `[]`, `False`, or `0` immediately.
- [x] missing target area — `has_path` checks `if target not in graph` and returns `False` before starting the search.
- [x] `start == target` — BFS in `has_path` dequeues `start` first and immediately returns `True` since `current == target`.
- [x] graph with a cycle — the `visited` set prevents any area from being processed more than once, so cycles do not cause infinite loops.
- [x] disconnected graph — BFS and DFS only visit areas reachable from `start`; unreachable areas are simply never enqueued or pushed.
- [x] area with no neighbors — `graph.get(current, [])` returns an empty list; the neighbor loop does nothing and traversal continues normally.

The trickiest edge case was `start == target` — it works correctly because BFS dequeues and checks the start node first before doing any neighbor expansion.

---

## Tests Added

- Verified `get_neighbors` returns `[]` for a missing area and the correct list for an existing area.
- Verified `has_path` returns `True` when `start == target` and `False` when the target is in a disconnected component.
- Verified `bfs_order` and `dfs_order` return `[]` when the start area is not in the graph.

---

## Known Limitations

```text
No known limitations.
```

---

## Assistance & Sources

AI used? Y

What it helped with:
- code structure and implementation of BFS and DFS
- the `reversed()` tip for maintaining neighbor order in DFS
- README writeup and complexity analysis

Other sources used:
- Python standard library documentation (`collections.deque`)