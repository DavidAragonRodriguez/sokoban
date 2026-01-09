#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: algoritmo_busqueda.py                             #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 04/11/2024                                         #
# Descripción del fichero: Contiene funciones útiles para aplicar el    #
# algoritmo de búsqueda y encontrar una solución (si la hay).           #
# Para ello, también cuenta con un método que asigna valores a los      #
# nodos dependiendo de la estrategia solicitada.                        #
#                                                                       #
#########################################################################

""" Importamos los módulos necesarios para ejecutar el código """
import estado_nivel
import frontera
import nodo
import funcion_sucesor

from constantes import EN_ANCHURA, EN_PROFUNDIDAD, COSTO_UNIFORME, VORAZ, A_ESTRELLA
from constantes import NO_ACCION, MSJ_NO_SOLUCION, TRUE_STR

def asignar_valor_nodo(nodo_entrada: nodo.Nodo, estrategia: str) -> None:
    """
    Nombre de la función: asignar_valor_nodo

    Descripción de la función: Asigna el valor correcto al nodo según la estrategia

    Parámetros de entrada:
        nodo_entrada (nodo.Nodo): Nodo al que vamos a asigarle su valor según la estrategia
        estrategia (estrategia): Estrategia que vamos a seguir
    """

    if estrategia == EN_ANCHURA:
        nodo_entrada.valor = nodo_entrada.profundidad

    elif estrategia == EN_PROFUNDIDAD:
        nodo_entrada.valor = 1 / (nodo_entrada.profundidad + 1)

    elif estrategia == COSTO_UNIFORME:
        nodo_entrada.valor = nodo_entrada.costo

    elif estrategia == VORAZ:
        nodo_entrada.estado.funcion_heuristica()
        nodo_entrada.valor = nodo_entrada.estado.heuristica

    elif estrategia == A_ESTRELLA:
        nodo_entrada.estado.funcion_heuristica()
        nodo_entrada.valor = nodo_entrada.costo + nodo_entrada.estado.heuristica

    else:
        nodo_entrada.valor = 0.00

def resolver_algoritmo(estado_inicial: estado_nivel.EstadoNivel,
                        nivel: str, estrategia: str, profundidad_max: int) -> str:
    """
    Nombre de la función: resolver_algoritmo

    Descripción de la función: Algoritmo de resolución para calcular una solución del nivel,
    si existe, a partir del estado inicial

    Parámetros de entrada:
        estado_inicial (estado_nivel.EstadoNivel): Estado inicial en el que se encuentra el nivel
        nivel (str): Nivel que queremos solucionar
        estrategia (str): Estrategia que vamos a seguir
        profundidad_max (int): Profundidad máxima de los nodos que vamos a expandir

    Valores de retorno:
        str: Camino solución o, si no hay solución, 'No solution'
    """

    front = frontera.Frontera()
    estados_visitados = list()

    nodo_inicial = nodo.Nodo((NO_ACCION, estado_inicial, 0), None)
    asignar_valor_nodo(nodo_inicial, estrategia)
    front.insertar(nodo_inicial)

    solucion_encontrada = False

    while front.hay_nodos() and not solucion_encontrada:

        nodo_actual = front.extraer()
        estado_actual = nodo_actual.estado

        if estado_actual.funcion_objetivo() == TRUE_STR:
            solucion_encontrada = True

        elif (nodo_actual.profundidad < profundidad_max and
            estado_actual.id_nivel not in estados_visitados):

            estados_visitados.append(estado_actual.id_nivel)
            sucesores_validos = funcion_sucesor.funcion_sucesores(nodo_actual.estado)

            for sucesor in sucesores_validos:       # sucesor: (acción, estado, coste_acción)

                nodo_sucesor = nodo.Nodo(sucesor, nodo_actual)
                asignar_valor_nodo(nodo_sucesor, estrategia)
                front.insertar(nodo_sucesor)

    if solucion_encontrada:

        camino_solucion = nodo_actual.obtener_camino()
        solucion = nivel

        for nodo_camino in camino_solucion:
            solucion += "\n" + nodo_camino.info_nodo()

    else:
        solucion = MSJ_NO_SOLUCION

    return solucion
