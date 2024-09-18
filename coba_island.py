graph = [[0, 1, 1, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 1, 0]]


def search_max_dg(G):
    dgr_node = sum(G[0])
    node = 0
    for i in range(len(G)):
        if sum(G[i]) >= dgr_node:
            dgr_node = i
            node = i
    return node


print(search_max_dg(graph))
