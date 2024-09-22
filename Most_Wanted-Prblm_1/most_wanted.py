LIMITE_INFERIOR = 0
LIMITE_SUPERIOR = 10


class Polices:
    def __init__(self, polices, ovi_pos):
        self.polices = polices
        self.turn = [0] * len(polices)
        self.ovi_pos = ovi_pos

    def police_turn(self):
        for i in self.polices:
            if i - 1 >= LIMITE_INFERIOR and i - 1 not in self.polices:
                # puede moverse a la izquierda
                pass
            if i + 1 <= LIMITE_SUPERIOR and i + 1 not in self.polices:
                # puede moverse a la derecha
                pass


def simular_movimiento(ovidio, policias):
    # Limites de la cuadrícula

    def mover_policias(policias, ovidio):
        nuevas_posiciones = set()
        eliminados = 0
        policias.sort()  # Ordenamos los policías para que se muevan en orden desde la izquierda

        for p in policias:
            # Determinar la dirección en la que el policía debe moverse para acercarse a Ovidio
            if p < ovidio:
                posibles_movimientos = [p + 1, p - 1]  # Prioriza moverse hacia la derecha (más cerca de Ovidio)
            else:
                posibles_movimientos = [p - 1, p + 1]  # Prioriza moverse hacia la izquierda

            movido = False
            for nuevo in posibles_movimientos:
                # El policía solo puede moverse si la nueva posición está dentro de los límites y no está ocupada
                if LIMITE_INFERIOR <= nuevo <= LIMITE_SUPERIOR and nuevo not in policias and nuevo != ovidio and nuevo not in nuevas_posiciones:
                    nuevas_posiciones.add(nuevo)
                    movido = True
                    break

            if not movido:
                eliminados += 1  # Policía eliminado si no puede moverse

        return list(nuevas_posiciones), eliminados

    def mover_ovidio(ovidio, policias):
        # Ovidio intenta alejarse de los policías más cercanos
        distancia_mas_cercana = min(abs(ovidio - p) for p in policias)
        movimiento_preferido = None

        # Ver si moverse hacia la izquierda es más seguro
        if LIMITE_INFERIOR <= ovidio - 1 and (ovidio - 1 not in policias):
            distancia_si_mueve_izquierda = min(abs((ovidio - 1) - p) for p in policias)
            if distancia_si_mueve_izquierda > distancia_mas_cercana:
                movimiento_preferido = ovidio - 1

        # Ver si moverse hacia la derecha es más seguro
        if LIMITE_SUPERIOR >= ovidio + 1 and (ovidio + 1 not in policias):
            distancia_si_mueve_derecha = min(abs((ovidio + 1) - p) for p in policias)
            if distancia_si_mueve_derecha > distancia_mas_cercana and (
                    movimiento_preferido is None or distancia_si_mueve_derecha > distancia_mas_cercana):
                movimiento_preferido = ovidio + 1

        # Si encontró un movimiento preferido, se mueve. Si no, es capturado
        if movimiento_preferido is not None:
            return movimiento_preferido, False  # Ovidio se mueve
        return ovidio, True  # Ovidio es capturado si no puede moverse

    eliminados_totales = 0
    capturado = False

    while policias and not capturado:
        # Movimiento de los policías
        policias, eliminados = mover_policias(policias, ovidio)
        eliminados_totales += eliminados

        # Movimiento de Ovidio
        ovidio, capturado = mover_ovidio(ovidio, policias)

    if capturado:
        return eliminados_totales, "Ovidio es capturado"
    else:
        return eliminados_totales, "Ovidio escapa"


# Ejemplo de uso:
C = 1  # Posición inicial de Ovidio
P = [2]  # Posiciones iniciales de los policías

resultado = simular_movimiento(C, P)
print(f"Eliminados: {resultado[0]}, Resultado: {resultado[1]}")
