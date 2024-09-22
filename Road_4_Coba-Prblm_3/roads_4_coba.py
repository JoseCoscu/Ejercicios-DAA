from coba_island import Node, Graph


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
        rank=[]
        for i in range(0, len(alt_g.nodes)):
            parent.append(i)
            rank.append(1)

        if alt_g.is_conx():
            edges_kruskal = []
            alt_g.edges.sort(key=lambda x: x[2])
            for i in alt_g.edges:
                x_parent = alt_g.set_of(parent, i[0].id)
                y_parent = alt_g.set_of(parent, i[1].id)
                if (x_parent != y_parent):
                    edges_kruskal.append(i)

                    # if rank[x_parent]>rank[y_parent]:
                    #     parent[i[1].id] = x_parent
                    #     rank[y_parent] -= 1
                    #     rank[x_parent] += 1
                    #
                    # else:
                    #     parent[i[0].id] = y_parent
                    #     rank[y_parent]+=1
                    #     rank[x_parent]-=1

                    if rank[i[0].id] < rank[i[1].id]:
                        parent[i[0].id] = i[1].id
                    elif rank[i[0].id] > rank[i[1].id]:
                        parent[i[1].id] = i[0].id

                        # If ranks are same, then make one as root
                        # and increment its rank by one
                    else:
                        parent[i[1].id] = i[0].id
                        rank[i[0].id] += 1

            return edges_kruskal
        else:
            return ' no es un grafo conexo'

    def set_of(self, parent, id):
        if parent[id] == id:
            return id
        new_id = parent[id]
        return self.set_of(parent, new_id)


# class Grafo:
#     def __init__(self, nodes: list):
#         self.V = nodes
#         self.grafo = []
#
#     def agregar_arista(self, u, v, w):
#         self.grafo.append([u, v, w])
#
#     def buscar(self, padre, i):
#         if padre[i] == i:
#             return i
#         return self.buscar(padre, padre[i])
#
#     def union(self, padre, rango, x, y):
#         x_raiz = self.buscar(padre, x)
#         y_raiz = self.buscar(padre, y)
#
#         if rango[x_raiz] < rango[y_raiz]:
#             padre[x_raiz] = y_raiz
#         elif rango[x_raiz] > rango[y_raiz]:
#             padre[y_raiz] = x_raiz
#         else:
#             padre[y_raiz] = x_raiz
#             rango[x_raiz] += 1
#
#     def kruskal(self):
#         resultado = []
#         i, e = 0, 0
#         self.grafo = sorted(self.grafo, key=lambda item: item[2])
#         padre = []
#         rango = []
#
#         for nodo in range(self.V):
#             padre.append(nodo)
#             rango.append(0)
#
#         while e < self.V - 1:
#             u, v, w = self.grafo[i]
#             i += 1
#             x = self.buscar(padre, u)
#             y = self.buscar(padre, v)
#
#             if x != y:
#                 e += 1
#                 resultado.append([u, v, w])
#                 self.union(padre, rango, x, y)
#
#         return resultado
#
#
# # Ejemplo de uso
# g = Grafo(4)
# g.agregar_arista(0, 1, 10)
# g.agregar_arista(0, 2, 6)
# g.agregar_arista(0, 3, 5)
# g.agregar_arista(1, 3, 15)
# g.agregar_arista(2, 3, 4)
#
# arbol_recubridor_minimo = g.kruskal()
# for u, v, w in arbol_recubridor_minimo:
#     print(f"Arista {u} - {v} con peso {w}")

nodes = [P_Node(0, 1), P_Node(1, 2), P_Node(2, 1), P_Node(3, 2)]

g = P_Graph(nodes)

g.connect_nodes_weight(nodes[0], nodes[1], 0)
g.connect_nodes_weight(nodes[2], nodes[3], 0)
g.connect_nodes_weight(nodes[0], nodes[2], 1)
g.connect_nodes_weight(nodes[1], nodes[3], 2)

e = g.get_max_tree()
print(e)

# parent=[1,2,2,0]
# def set_of(parent, id):
#     if parent[id] == id:
#         return id
#     new_id = parent[id]
#     return set_of(parent, new_id)
#
# print(set_of(parent,3))