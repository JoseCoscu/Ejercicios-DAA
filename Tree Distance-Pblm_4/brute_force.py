import itertools
from collections import defaultdict, deque


def generate_trees(n):
    """Genera todos los árboles no etiquetados con n vértices."""
    if n == 1:
        yield {0: []}
        return

    vertices = list(range(n))
    # Generar todas las combinaciones de aristas posibles
    for edges in itertools.combinations(itertools.combinations(vertices, 2), n - 1):
        adjacency_list = defaultdict(list)

        # Construir la lista de adyacencia
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # Verificar si es un árbol
        if is_tree(adjacency_list, n):
            yield adjacency_list


def is_tree(adjacency_list, n):
    """Verifica si el grafo es un árbol (conectado y sin ciclos)."""
    visited = set()
    queue = deque([0])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(visited) == n and all(len(adjacency_list[v]) > 0 for v in range(n))


def count_vertices_by_level(tree):
    """Cuenta la cantidad de vértices en niveles pares e impares."""
    level_count = {0: 0, 1: 0}  # {nivel_par: count, nivel_impar: count}

    def bfs_count_levels(start_node):
        queue = deque([(start_node, 0)])  # (nodo actual, nivel)
        visited = set()

        while queue:
            current_node, level = queue.popleft()

            if current_node not in visited:
                visited.add(current_node)
                level_count[level % 2] += 1  # Incrementar según el nivel par/impar

                for neighbor in tree[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, level + 1))

    bfs_count_levels(0)  # Comenzar desde el nodo raíz (0)

    return level_count[0], level_count[1]  # (pares, impares)


def calculate_distance(tree, u, v):
    """Calcula la distancia entre dos vértices en el árbol usando BFS."""
    if u == v:
        return 0

    queue = deque([(u, 0)])  # (nodo actual, distancia)
    visited = set()

    while queue:
        current_node, distance = queue.popleft()

        if current_node == v:
            return distance

        visited.add(current_node)

        for neighbor in tree[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return float(
        "inf"
    )  # En caso de que no se encuentre (no debería suceder en un árbol)


def count_pairs(tree):
    """Cuenta los pares de vértices con distancias par e impar."""
    distances = defaultdict(int)
    vertices = list(tree.keys())

    for u in vertices:
        for v in vertices:
            distance = calculate_distance(tree, u, v)
            distances[distance % 2] += 1  # 0 para par, 1 para impar

    return distances[0], distances[1]


def find_tree_with_distances(x, y):
    """Encuentra un árbol que cumpla con las condiciones de pares de distancias."""
    total_pairs = x + y
    n = int(total_pairs**0.5)  # Calcular el número de vértices

    if n * n != total_pairs:  # Asegurarse de que sea un cuadrado perfecto
        return None

    for tree in generate_trees(n):
        even_count, odd_count = count_pairs(tree)
        if even_count == x and odd_count == y:
            return tree
    return None


# Ejemplo de uso
x = 8  # Pares con distancia par
y = 8  # Pares con distancia impar

result = find_tree_with_distances(x, y)
if result:
    print("Árbol encontrado:", result)

    # Contar vértices en niveles pares e impares
    even_vertices, odd_vertices = count_vertices_by_level(result)

    print(f"Cantidad de vértices en niveles pares: {even_vertices}")
    print(f"Cantidad de vértices en niveles impares: {odd_vertices}")
else:
    print("No se encontró ningún árbol que cumpla las condiciones.")
