#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: sokoban.py                                        #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 23/09/2024                                         #
# Descripción del fichero: Contiene el main, que lee la línea de        #
# comandos y, según la tarea solicitada, realiza una acción u otra.     #
#                                                                       #
#########################################################################

""" Importamos las librerías y módulos necesarios para ejecutar el código """
import sys
import argparse

import estado_nivel
import funcion_sucesor
import algoritmo_busqueda

from constantes import MURO, JUGADOR, CAJA, OBJETIVO, CAJA_EN_OBJETIVO, JUGADOR_EN_OBJETIVO, VACIO
from constantes import TAREA1, TAREA2_SUCESORES, TAREA2_OBJETIVO, TAREA3

def comprobar_nivel(nivel: str) -> bool:
    """
    Nombre del método: comprobar_nivel

    Descripción del método: Comprueba que la cadena de caracteres que
    representa el nivel tenga elementos válidos

    Parámetros de entrada:
        nivel (str): Nivel del sokoban a comprobar

    Valores de retorno:
        bool: Devuelve si el nivel es válido o no
    """

    filas_nivel = nivel.split('\\n')

    valido = True
    elem_validos = [MURO, JUGADOR, CAJA, OBJETIVO, CAJA_EN_OBJETIVO, JUGADOR_EN_OBJETIVO, VACIO]
    num_jugadores = num_cajas = num_objetivos = 0

    for fila in filas_nivel:

        for elemento in fila:

            if elemento not in elem_validos:
                valido = False

            if elemento == JUGADOR:
                num_jugadores += 1
            elif elemento == CAJA:
                num_cajas += 1
            elif elemento == OBJETIVO:
                num_objetivos += 1
            elif elemento == CAJA_EN_OBJETIVO:
                num_cajas += 1
                num_objetivos += 1
            elif elemento == JUGADOR_EN_OBJETIVO:
                num_jugadores += 1
                num_objetivos += 1

    if num_jugadores != 1 or num_cajas > num_objetivos or num_cajas < 1:
        valido = False

    return valido

def main():
    """
    Nombre del método: main

    Descripción del método: Lectura de la línea de comandos y
    llamada a las diferentes tareas

    Control excepciones: Se comprueba que el comando usado sea correcto
    y el nivel del sokoban válido
    """

    parser = argparse.ArgumentParser(description = "Sokoban")

    parser.add_argument(
        'tarea',
        choices = ['T1', 'T2S', 'T2T', 'T3'],
        help = "Tarea a realizar"
    )

    parser.add_argument(
        '-l', '--level',
        metavar = '<nivel>',
        help = "Nivel del sokoban (string)",
        required = True
    )

    parser.add_argument(
        '-s', '--strategy',
        choices = ['BFS', 'DFS', 'UC', 'GREEDY', 'A*'],
        help = "Estrategia a utilizar",
        required = False
    )

    parser.add_argument(
        '-d', '--depth',
        type = int,
        help = "Máxima profundidad",
        required = False
    )

    try:
        args = parser.parse_args()

        if not comprobar_nivel(args.level):
            print("Nivel incorrecto. Vuelva a ejecutar el programa con un nivel válido.\n")
            sys.exit(1)

        estado_inicial = estado_nivel.EstadoNivel(args.level)

        if args.tarea == TAREA1:
            estado_inicial.mostrar_info_nivel()

        elif args.tarea == TAREA2_SUCESORES:
            funcion_sucesor.mostrar_info_sucesores(estado_inicial)

        elif args.tarea == TAREA2_OBJETIVO:
            print(estado_inicial.funcion_objetivo())

        elif args.tarea == TAREA3:

            if args.strategy is None or args.depth is None:
                print("Para la tarea T3, los parámetros -s y -d son obligatorios.\n")
                sys.exit(2)

            print(algoritmo_busqueda.resolver_algoritmo(
                estado_inicial, args.level, args.strategy, args.depth))

        else:
            print("La tarea solicitada no existe, vuelva a ejecutar el programa.\n")
            sys.exit(3)

    except SystemExit:
        print("\nUso incorrecto de la línea de comandos.")
        sys.exit(4)

if __name__ == "__main__":
    main()
