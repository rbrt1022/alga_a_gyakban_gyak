#https://www.hackerrank.com/challenges/johnland/problem

def roadsInHackerland(n, roads):
    roads.sort(key=lambda x: x[2])

    parent = list(range(n + 1))
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    mst_adj = [[] for _ in range(n + 1)]
    edges_count = 0
    
    for u, v, c in roads:
        if union(u, v):
            mst_adj[u].append((v, c))
            mst_adj[v].append((u, c))
            edges_count += 1
            if edges_count == n - 1:
                break

    weights = {} 

    def dfs(u, p):
        subtree_size = 1
        for v, c in mst_adj[u]:
            if v != p:
                child_size = dfs(v, u)
                paths = child_size * (n - child_size)
                weights[c] = weights.get(c, 0) + paths
                subtree_size += child_size
        return subtree_size

    dfs(1, -1)

    result = []
    carry = 0
    i = 0
    
    while weights or carry:
        val = weights.pop(i, 0) + carry
        result.append(str(val % 2))
        carry = val // 2
        i += 1

    return "".join(result[::-1])
