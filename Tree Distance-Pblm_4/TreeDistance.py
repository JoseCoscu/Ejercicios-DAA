import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def print_tree(node, level=0):
    print(" " * level * 4 + str(node.value))
    for child in node.children:
        print_tree(child, level + 1)


def create_tree(a, b):
    root = Node("Root")

    # Agregar nodos en niveles pares
    for i in range(a):
        root.add_child(Node(f"I{i+1}"))  # Nodos en nivel par

    # Agregar nodos en niveles impares
    for i in range(b):
        root.children[0].add_child(
            Node(f"P{i+1}")
        )  # Nodos en nivel impar bajo el primer nodo par

    return root


def find_pairs(node, level=0, pairs=None):
    if pairs is None:
        pairs = {"even": [], "odd": []}

    # Obtener todos los hijos
    for child in node.children:
        # Si el nivel es par, los hijos son impares
        if level % 2 == 0:
            pairs["even"].append((node.value, child.value))
        else:
            pairs["odd"].append((node.value, child.value))

        # Llamar recursivamente para los hijos
        find_pairs(child, level + 1, pairs)

    return pairs


def find_tree_structure(x, y):
    # Iterar sobre posibles valores para a
    for kA in range(int((x + y) ** 0.5) + 1):
        # Calcular b usando la fórmula derivada
        kB_squared = x - kA**2
        if kB_squared < 0:
            continue

        kB = int(kB_squared**0.5)

        if kA**2 + kB**2 == x and 2 * kA * kB == y:
            return (kA, kB)

    return None


def draw_tree(root):
    G = nx.DiGraph()  # Crear un grafo dirigido

    def add_edges(node):
        for child in node.children:
            G.add_edge(node.value, child.value)  # Agregar arista del nodo padre al hijo
            add_edges(child)  # Llamar recursivamente para los hijos

    add_edges(root)  # Llenar el grafo con aristas

    pos = nx.spring_layout(G)  # Posicionamiento de los nodos
    nx.draw(G, pos, with_labels=True, arrows=True)

    plt.title("Representación del Árbol")
    plt.axis("off")  # Ocultar los ejes
    plt.show()


# Ejemplo de uso
x = 8  # Número de pares con distancia par
y = 8  # Número de pares con distancia impar

# Encontrar a y b
result = find_tree_structure(x, y)

if result:
    a, b = result
    print(f"Vértices en niveles impares: {a}, Vértices en niveles pares: {b}")

    # Crear y mostrar el árbol
    tree_root = create_tree(a, b)

    # print("Representación del árbol:")
    # print_tree(tree_root)

    # Dibujar el árbol usando matplotlib y networkx
    # draw_tree(tree_root)

else:
    print("No se encontró una solución válida.")
