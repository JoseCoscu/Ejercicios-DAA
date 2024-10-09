import matplotlib.pyplot as plt
import networkx as nx
from coba_island import *
import threading
import sys
import time

l1 = 0
l2 = 0
l3 = 0


# Función que muestra el mensaje de "procesando..." con puntos animados
def procesando():
    while not finalizar.is_set():
        for i in range(4):  # Repite de 0 a 3 puntos
            if finalizar.is_set():
                break
            sys.stdout.write("\rProcesando" + "." * i + " " * (3 - i))
            sys.stdout.flush()
            time.sleep(0.5)  # Pausa de 0.5 segundos entre cada punto


# Crear un evento para detener el hilo
finalizar = threading.Event()

# Inicia el hilo para la animación de "procesando..."
hilo_procesando = threading.Thread(target=procesando)
hilo_procesando.start()

# Aquí colocas el resto del código del programa
# Simulando una tarea larga
try:
    for i in range(10):
        G = crear_grafo_aleatorio_bi(20)

        setcover, sets = G.set_cover()
        guardians = G.get_guardians()
        print(setcover)
        print(guardians)

        if abs(len(setcover) - len(guardians)) == 1:
            l1 += 1
        if abs(len(setcover) - len(guardians)) == 2:
            l2 += 1
        if abs(len(setcover) - len(guardians)) == 3:
            l3 += 1

finally:
    # Al terminar la tarea, señalizamos el evento de finalización
    finalizar.set()
    # Esperamos a que el hilo termine
    hilo_procesando.join()

# Limpiar la línea de procesamiento al finalizar
sys.stdout.write("\rProceso completado.         \n")



diferencias = [l1, l2, l3]
etiquetas = [f'1 elemento: {l1} ', f'2 elementos: {l2}', f'3 elementos: {l3}']

# Crear gráfica de barras
plt.bar(etiquetas, diferencias, color=['blue', 'orange', 'green'])

# Agregar títulos y etiquetas
plt.title('Comparación de diferencias entre Greedy y Fuerza Bruta')
plt.xlabel('Diferencia en número de elementos')
plt.ylabel('Cantidad de ocurrencias')


# Mostrar la gráfica
plt.show()
