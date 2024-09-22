# graph = [[0, 1, 1, 1, 0, 0, 0],
#          [1, 0, 0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 1, 0, 0],
#          [1, 0, 0, 0, 1, 0, 0],
#          [0, 0, 1, 1, 0, 1, 0],
#          [0, 0, 0, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0, 1, 0]]
import copy
import itertools


class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    @property
    def degr(self):
        drg = len(self.neighbors)
        return drg

    def __repr__(self):
        return f"Node:{self.id}"

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    def __hash__(self):
        # Usamos el id del nodo como su valor hash, ya que se supone que el id es único para cada nodo
        return hash(self.id)


def set_cover(U, S):
    U_prime = set(U)  # Los elementos no cubiertos inicialmente son el universp
    C = []  # El conjunto solución (conjuntos seleccionados)

    while U_prime:
        # Seleccionar el subconjunto que cubre el mayor número de elementos aún no cubiertos
        best_set = max(S, key=lambda s: len(s & U_prime))

        # Añadir el subconjunto seleccionado al conjunto solución
        C.append(best_set)

        # Eliminar los elementos cubiertos por el subconjunto seleccionado
        U_prime -= best_set

    return C


class Graph:
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.edges = []

    def connect_nodes(self, node1: Node, node2: Node):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        self.edges.append((node1, node2))

    def search_max_dg_bf(self):
        node = self.nodes[0]
        nodes = [node]
        for i in self.nodes:
            if i.degr > node.degr:
                node = i
            elif i.degr >= node.degr:
                nodes.append(i)
        return nodes

    def remove_nodes(self, nodes_to_remove: list):

        #eliminando aristas
        for i in nodes_to_remove:
            for e in range(len(self.edges)):
                if i in self.edges[e]:
                    self.edges.pop(e)

        # Eliminar nodos de la lista de nodos del grafo
        self.nodes = [node for node in self.nodes if node not in nodes_to_remove]

        # Eliminar los nodos de la lista de vecinos de los nodos restantes
        for node in self.nodes:
            node.neighbors = [neighbor for neighbor in node.neighbors if neighbor not in nodes_to_remove]

    def get_subsets(self):
        subconjuntos = []
        # Iterar sobre todos los tamaños posibles de subconjuntos (de 0 a len(lista))
        for r in range(len(self.nodes) + 1):
            # Generar todas las combinaciones de tamaño r
            subconjuntos.extend(itertools.combinations(self.nodes, r))

        return subconjuntos

    def get_guardians(self):
        subs = list(self.get_subsets())
        subs.pop(0)

        for i in subs:
            temp_graph = Graph(copy.deepcopy(self.nodes))
            # Crear un conjunto de todos los nodos a remover: los nodos dados + sus vecinos
            nodes_and_neighbors = set(i)
            for node in i:
                nodes_and_neighbors.update(node.neighbors)

            # Remover los nodos y sus vecinos del grafo temporal
            temp_graph.remove_nodes(list(nodes_and_neighbors))
            if temp_graph.nodes:
                continue
            return i

    def set_cover(self):
        S = []
        for i in G.nodes:
            S.append({i}.union(i.neighbors))
        U_prime = set(self.nodes)  # Los elementos no cubiertos inicialmente son el univerdso
        C = []  # El conjunto solución (conjuntos seleccionados)

        while U_prime:
            # Seleccionar el subconjunto que cubre el mayor número de elementos aún no cubiertos
            best_set = max(S, key=lambda s: len(s & U_prime))

            # Añadir el subconjunto seleccionado al conjunto solución
            C.append(best_set)

            # Eliminar los elementos cubiertos por el subconjunto seleccionado
            U_prime -= best_set

        return C



nodes = []

for i in range(0, 7):
    nodes.append(Node(i))

G = Graph(nodes)

G.connect_nodes(nodes[0], nodes[1])
G.connect_nodes(nodes[0], nodes[2])
G.connect_nodes(nodes[0], nodes[3])
G.connect_nodes(nodes[3], nodes[4])
G.connect_nodes(nodes[2], nodes[4])
G.connect_nodes(nodes[4], nodes[5])
G.connect_nodes(nodes[5], nodes[6])

S = []

for i in G.nodes:
    S.append({i}.union(i.neighbors))


c = G.set_cover()

# Ejemplo de uso
# mi_lista = [1, 2, 3]
# # subconjuntos = obtener_subconjuntos(mi_lista)
#
# # Imprimir los subconjuntos
# for subconjunto in subconjuntos:
#     print(subconjunto)
guardians = G.get_guardians()
print(guardians)
print(c)
