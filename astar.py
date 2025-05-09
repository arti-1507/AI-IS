import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.h = {}

    def add(self, u, v, cost):
        self.graph.setdefault(u, []).append((v, cost))
        self.graph.setdefault(v, []).append((u, cost))  # Undirected

    def set_heuristic(self, h):
        self.h = h

    def astar(self, start, goal):
        q = [(self.h[start], 0, start, [])]
        visited = set()
        while q:
            f, g, node, path = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node]
            if node == goal:
                return path
            for neigh, cost in self.graph.get(node, []):
                if neigh not in visited:
                    heapq.heappush(q, (g + cost + self.h.get(neigh, 0), g + cost, neigh, path))
        return None

# Input
g = Graph()
for _ in range(int(input("Edges: "))):
    u, v, c = input("u v cost: ").split()
    g.add(u, v, int(c))

h = {}
for _ in range(int(input("Nodes with heuristics: "))):
    n, val = input("node heuristic: ").split()
    h[n] = int(val)
g.set_heuristic(h)

s = input("Start: ")
e = input("Goal: ")

# Output
res = g.astar(s, e)
print("Path:", res if res else "Not found")
