import random
from brute_force import *
from TreeDistance import *


def generate_pairs(num_pairs=100):
    pairs = []
    for _ in range(num_pairs):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        pairs.append((x, y))
    return pairs


def compare_algorithms(pairs):
    results_algo1 = []
    results_algo2 = []

    for x, y in pairs:
        result1 = find_tree_with_distances(x, y)
        result2 = find_tree_structure(x, y)

        results_algo1.append(result1)
        results_algo2.append(result2)

    return results_algo1, results_algo2


# Generar pares (x, y)
pairs_to_compare = generate_pairs()

# Comparar resultados de ambos algoritmos
results_algo1, results_algo2 = compare_algorithms(pairs_to_compare)

# Imprimir resultados de comparación
for i, (pair, result1, result2) in enumerate(
    zip(pairs_to_compare, results_algo1, results_algo2)
):
    x, y = pair
    print(f"Par (x={x}, y={y}):")
    print(f"Resultado Algoritmo 1: {result1}")
    print(f"Resultado Algoritmo 2: {result2}")
    print("-" * 40)
