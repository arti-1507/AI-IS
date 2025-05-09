def dfs(adj, v, visited):
    visited[v] = True
    print(v, end=" ")
    for u in adj[v]:
        if not visited[u]:
            dfs(adj, u, visited)

if __name__ == "__main__":
    V = int(input("Vertices: "))
    adj = [[] for _ in range(V)]
    for _ in range(int(input("Edges: "))):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    start = int(input("Start DFS from: "))
    dfs(adj, start, [False] * V)
