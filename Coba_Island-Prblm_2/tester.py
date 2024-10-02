import matplotlib.pyplot as plt
import networkx as nx
from coba_island import *


coutn1 = []
coutn2 = []
coutn3 = []
#
# for i in range(1000):
#     G = crear_grafo_aleatorio(20)
#
#     setcover, sets = G.set_cover()
#     guardians = G.get_guardians()
#
#     if abs(len(setcover) - len(guardians)) == 1:
#         coutn1.append(1)
#     if abs(len(setcover) - len(guardians)) == 2:
#         coutn2.append(2)
#     if abs(len(setcover) - len(guardians)) == 3:
#         coutn3.append(3)
#
#     print(guardians)  # Fuerza Bruta
#     print(setcover)  # Greedy
#
# print(coutn1)
# print(len(coutn1))
#
# print(coutn2)
# print(len(coutn2))
#
# print(coutn3)
# print(len(coutn3))


# Define las listas
lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
lista3 = [1.5, 3.5, 5.5, 7.5, 9.5]

# Crea los datos para la gráfica
x = range(len(lista1))  # Índice de cada elemento
y1 = lista1
y2 = lista2
y3 = lista3

# Crea la gráfica
plt.plot(x, y1, label='Lista 1', marker='o', linestyle='-')
plt.plot(x, y2, label='Lista 2', marker='s', linestyle='--')
plt.plot(x, y3, label='Lista 3', marker='^', linestyle='-.')

# Añade etiquetas a los ejes
plt.xlabel('Índice')
plt.ylabel('Valor')

# Añade una leyenda
plt.legend()

# Muestra la gráfica
plt.show()

# Crear un grafo aleatorio con 10 nodos
grafo_aleatorio = crear_grafo_aleatorio(10)

# Mostrar el grafo
print(grafo_aleatorio.nodes)  # Muestra los nodos
print(grafo_aleatorio.edges)  # Muestra las aristas

# Visualizar el grafo
nx.draw(grafo_aleatorio, with_labels=True)
plt.show()


