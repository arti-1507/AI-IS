from collections import deque

def bfs(adj, start):
    visited = [False] * len(adj)
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=" ")
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)

if __name__ == "__main__":
    V = int(input("Vertices: "))
    adj = [[] for _ in range(V)]
    for _ in range(int(input("Edges: "))):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    start = int(input("Start BFS from: "))
    bfs(adj, start)
