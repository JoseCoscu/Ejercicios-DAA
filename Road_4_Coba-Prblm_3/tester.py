from roads_4_coba import *
import random


def crear_grafo_aleatorio(n_nodos):
    """
    Crea un grafo aleatorio con n_nodos nodos.

    Args:
        n_nodos: Un entero positivo que representa el número de nodos en el grafo.

    Returns:
        Un objeto de grafo NetworkX.
    """
    nodes = [P_Node(i, random.randint(1, 10)) for i in range(0, n_nodos)]

    # Crear un grafo vacío
    grafo = P_Graph(nodes)

    # Agregar aristas aleatoriamente
    for i in range(n_nodos):
        for j in range(i + 1, n_nodos):
            # Probabilidad aleatoria de agregar una arista
            if random.random() < 0.5:  # Ajusta la probabilidad aquí
                l = nodes[i].meaning & nodes[j].meaning if random.random() > 0.7 else random.randint(1, 10)
                if l != 0:
                    grafo.connect_nodes_weight(nodes[i], nodes[j], l)

    return grafo


for i in range(1):
    g = crear_grafo_aleatorio(20)
    brute = g.brute()
    greedy = g.get_max_tree()
    print(brute)
    print(greedy)
