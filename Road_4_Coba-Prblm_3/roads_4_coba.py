from coba_island import Node, Graph
import itertools


class P_Node(Node):
    def __init__(self, id, meaning):
        super().__init__(id)
        self.meaning = meaning
        self.visited = False


class P_Graph(Graph):
    def __init__(self, nodes: list):
        super().__init__(nodes)

    def is_conx(self):
        if self.nodes:
            node = self.nodes[0]
        else:
            return False
        queue = [node]
        node.visited = True
        while queue:
            v = queue.pop()
            for i in v.neighbors:
                if not i.visited:
                    i.visited = True
                    queue.append(i)

        for i in self.nodes:
            if not i.visited:
                return False

        return True

    def connect_nodes_weight(self, node1: Node, node2: Node, weight):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        self.edges.append((node1, node2, weight))

    def check_edges(self):
        posible_edges = []
        for i in self.edges:
            if (i[0].meaning & i[1].meaning & i[2]) == i[2]:
                posible_edges.append(i)

        return posible_edges

    def get_max_tree(self):
        p_edges = self.check_edges()  # Verifica las aristas q cumplen la condicion
        nodes = []
        for e in p_edges:
            node1 = P_Node(e[0].id, e[0].meaning)
            node2 = P_Node(e[1].id, e[1].meaning)

            if node1 not in nodes: nodes.append(node1)
            if node2 not in nodes: nodes.append(node2)
            node1 = nodes[nodes.index(node1)]
            node2 = nodes[nodes.index(node2)]

            if node2 not in node1.neighbors: node1.neighbors.append(node2)
            if node1 not in node2.neighbors: node2.neighbors.append(node1)

        nodes.sort(key=lambda x: x.id)

        # Si no estan todos los nodos presentes en
        # en las aristas que cumplen la condicion
        # entonces no es posible conectar todos los nodos se devuelve -1
        if len(nodes) < len(self.nodes): return -1

        alt_g = P_Graph(nodes)
        alt_g.edges = p_edges
        parent = []
        rank = []
        for i in range(0, len(alt_g.nodes)):
            parent.append(i)
            rank.append(1)

        if alt_g.is_conx():
            edges_kruskal = []
            alt_g.edges.sort(key=lambda x: x[2])
            for i in alt_g.edges:
                x_parent = alt_g.set_of(parent, i[0].id)
                y_parent = alt_g.set_of(parent, i[1].id)
                if x_parent != y_parent:
                    edges_kruskal.append(i)

                    if rank[x_parent] < rank[y_parent]:###probar con el parent adentro rank del parent
                        parent[x_parent] = alt_g.set_of(parent, i[1].id)
                        rank[parent[i[0].id]] += 1
                    elif rank[x_parent] > rank[y_parent]:
                        parent[y_parent] = x_parent
                        rank[parent[i[1].id]] += 1
                        # If ranks are same, then make one as root
                        # and increment its rank by one
                    else:
                        parent[y_parent] = x_parent
                        rank[parent[i[1].id]] += 1
                    # if len(edges_kruskal)==len(nodes)-1:
                    #     count = 0
                    #     for i in edges_kruskal:
                    #         count += i[2]
                    #     return edges_kruskal, count

            count = 0
            for i in edges_kruskal:
                count += i[2]
            return edges_kruskal, count
        else:
            return -1

    def set_of(self, parent, id):
        if parent[id] == id:
            return id
        new_id = parent[id]
        return self.set_of(parent, new_id)

    def get_subsetss(self, iterable):
        subconjuntos = []
        # Iterar sobre todos los tamaños posibles de subconjuntos (de 0 a len(lista))
        for r in range(len(iterable) + 1):
            # Generar todas las combinaciones de tamaño r
            subconjuntos.extend(itertools.combinations(iterable, r))
        return subconjuntos

    def brute(self):
        edges = self.check_edges()
        sset = self.get_subsetss(edges)
        sset.pop(0)

        dic = {}
        for i in sset:
            cout = 0
            for j in i:
                cout += j[2]
            dic[i] = cout
        dic = dict(sorted(dic.items(), key=lambda x: x[1]))

        keys = list(dic.keys())
        for i in keys:
            nodes = [P_Node(i.id, i.meaning) for i in self.nodes]
            g = P_Graph(nodes)
            for j in i:
                node1 = nodes.index(j[0])
                node2 = nodes.index(j[1])
                g.connect_nodes(nodes[node1], nodes[node2])
            if g.is_conx():
                return i, dic[i]
        return -1

# nodes = [P_Node(0, 1), P_Node(1, 2), P_Node(2, 1), P_Node(3, 2)]
#
# g = P_Graph(nodes)
#
# g.connect_nodes_weight(nodes[0], nodes[1], 0)
# g.connect_nodes_weight(nodes[2], nodes[3], 0)
# g.connect_nodes_weight(nodes[0], nodes[2], 1)
# g.connect_nodes_weight(nodes[1], nodes[3], 2)
#
# l = g.brute()
# print(l)
#
# e = g.get_max_tree()
# print(e)
