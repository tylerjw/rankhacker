from pprint import pprint

def neighboors(paths, node):
    ret = set()
    for p in paths:
        if node is p[0]:
            ret.add(p[1])
        elif node is p[1]:
            ret.add(p[0])
    return ret

def dfs_iterative(paths, node):
    stack = [node]
    visited = set([node])
    while (len(stack)):
        v = stack.pop() # vertex from stack to visit next
        for n in neighboors(paths, v):
            if n not in visited:
                stack.append(n)
                visited.add(n)
    return visited

def node_groups(n_nodes, paths):
    r = set(range(n_nodes)) # remaining nodes
    groups = []
    while (len(r)):
        node = r.pop()
        group = dfs_iterative(paths, node)
        r = r.difference(group)
        groups.append(group)
    return groups

def floyd_warshall(n_nodes, paths):
    dist = [[float("inf") for x in range(n_nodes)] for y in range(n_nodes)]
    next_node = [[None for x in range(n_nodes)] for y in range(n_nodes)]
    for v in range(n_nodes):
        dist[v][v] = 0
    for u,v in paths:
        dist[u][v] = 1 # weight(u,v)
        dist[v][u] = 1 # weight(v,u)
        next_node[u][v] = v
        next_node[v][u] = u
    for k in range(n_nodes):
        for i in range(n_nodes):
            for j in range(n_nodes):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
                    next_node[j][i] = next_node[j][k]
        #pprint(dist)
        #pprint(next_node)
    return (dist, next_node)

def shortest_path(u, v, next_node):
    if (next_node[u][v] == None):
        return []
    path = [u]
    while (u != v):
        u = next_node[u][v]
        path.append(u)
    return path

n = 6 # number of cities
m = 6 # number of roads
roads = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
roads_index = [[u-1,v-1] for u,v in roads]
pprint(roads)
pprint(roads_index)

for city in range(n):
    print (city,neighboors(roads_index, city))

pprint (node_groups(n, roads_index))

dist, next_node = floyd_warshall(n, roads_index)
pprint ((dist, next_node))


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        print (str(i) + ' -> ' + str(j) + ': ', shortest_path(i,j,next_node)) 
