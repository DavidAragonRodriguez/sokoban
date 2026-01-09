#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: funcion_sucesor.py                                #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 14/10/2024                                         #
# Descripción del fichero: Contiene funciones útiles para calcular los  #
# sucesores de un estado.                                               #
#                                                                       #
#########################################################################

"""
Importamos la librería necesaria para la copia de listas y
el módulo necesario para almacenar el estado de un nivel
"""
import copy

import estado_nivel

from constantes import MOV_ARRIBA, MOV_DERECHA, MOV_ABAJO, MOV_IZQUIERDA

def comprobar_mov_valido_caja(estado_nuevo:estado_nivel.EstadoNivel, nueva_pos_caja:tuple) -> bool:
    """
    Nombre de la función: comprobar_mov_valido_caja

    Descripción de la función: Comprueba si se puede mover una caja en un estado dado de un nivel

    Parámetros de entrada:
        estado_nuevo (estado_nivel.EstadoNivel): Representa el estado posible sucesor
                                                 del estado actual del nivel
        nueva_pos_caja (tuple): Posición de la caja después del movimiento realizado

    Valores de retorno:
        bool: Indica si el movimiento de la caja es válido o no
    """

    mov_valido = True

    if nueva_pos_caja in estado_nuevo.lista_muros or nueva_pos_caja in estado_nuevo.lista_cajas:
        mov_valido = False

    return mov_valido

def obtener_sucesores_validos(estado_nuevo: estado_nivel.EstadoNivel, nueva_pos_jugador: tuple,
                                 movimiento: str, lista_sucesores: list) -> None:
    """
    Nombre de la función: obtener_sucesores_validos

    Descripción de la función: Añade a la lista pasada como parámetro las
    tuplas con los sucesores válidos de un nivel dado

    Parámetros de entrada:
        estado_nuevo (estado_nivel.EstadoNivel): Representa el nivel sucesor a verificar
        nueva_pos_jugador (tuple): Posición del jugador después del movimiento realizado
        movimiento (str): Movimiento realizado por el jugador ({'u', 'r', 'd', 'l'})
        lista_sucesores (list): Almacena los sucesores válidos de un estado.
                                Se añade el sucesor (estado_nuevo) si es válido
    """

    mov_valido = True
    mov_caja = False
    indice_caja_a_mover = -1

    if nueva_pos_jugador in estado_nuevo.lista_muros:
        mov_valido = False

    elif nueva_pos_jugador in estado_nuevo.lista_cajas:

        mov_caja = True
        indice_caja_a_mover = estado_nuevo.lista_cajas.index(nueva_pos_jugador)

        if movimiento == MOV_ARRIBA:

            nueva_pos_caja = (nueva_pos_jugador[0] - 1, nueva_pos_jugador[1])
            mov_valido = comprobar_mov_valido_caja(estado_nuevo, nueva_pos_caja)

        elif movimiento == MOV_DERECHA:

            nueva_pos_caja = (nueva_pos_jugador[0], nueva_pos_jugador[1] + 1)
            mov_valido = comprobar_mov_valido_caja(estado_nuevo, nueva_pos_caja)

        elif movimiento == MOV_ABAJO:

            nueva_pos_caja = (nueva_pos_jugador[0] + 1, nueva_pos_jugador[1])
            mov_valido = comprobar_mov_valido_caja(estado_nuevo, nueva_pos_caja)

        elif movimiento == MOV_IZQUIERDA:

            nueva_pos_caja = (nueva_pos_jugador[0], nueva_pos_jugador[1] - 1)
            mov_valido = comprobar_mov_valido_caja(estado_nuevo, nueva_pos_caja)

    if mov_valido and not mov_caja:

        estado_nuevo.pos_jugador = nueva_pos_jugador
        estado_nuevo.actualizar_id_nivel()

        lista_sucesores.append((movimiento, estado_nuevo, 1))

    elif mov_valido and mov_caja:

        estado_nuevo.pos_jugador = nueva_pos_jugador
        estado_nuevo.lista_cajas[indice_caja_a_mover] = nueva_pos_caja
        estado_nuevo.lista_cajas.sort()
        estado_nuevo.actualizar_id_nivel()

        lista_sucesores.append((movimiento.upper(), estado_nuevo, 1))

def funcion_sucesores(estado: estado_nivel.EstadoNivel) -> list:
    """
    Nombre de la función: funcion_sucesores

    Descripción de la función: Calcula los posibles sucesores válidos de un estado

    Parámetros de entrada:
        estado (estado_nivel.EstadoNivel): Representa el estado actual del nivel

    Valores de retorno:
        list: Lista con los sucesores válidos del estado actual
    """

    lista_sucesores = []

    estado_arriba = copy.deepcopy(estado)
    pos_jugador_arriba = (estado_arriba.pos_jugador[0] - 1, estado_arriba.pos_jugador[1])
    obtener_sucesores_validos(estado_arriba, pos_jugador_arriba, MOV_ARRIBA, lista_sucesores)

    estado_derecha = copy.deepcopy(estado)
    pos_jugador_derecha = (estado_derecha.pos_jugador[0], estado_derecha.pos_jugador[1] + 1)
    obtener_sucesores_validos(estado_derecha, pos_jugador_derecha, MOV_DERECHA, lista_sucesores)

    estado_abajo = copy.deepcopy(estado)
    pos_jugador_abajo = (estado_abajo.pos_jugador[0] + 1, estado_abajo.pos_jugador[1])
    obtener_sucesores_validos(estado_abajo, pos_jugador_abajo, MOV_ABAJO, lista_sucesores)

    estado_izquierda = copy.deepcopy(estado)
    pos_jugador_izqda = (estado_izquierda.pos_jugador[0], estado_izquierda.pos_jugador[1] - 1)
    obtener_sucesores_validos(estado_izquierda, pos_jugador_izqda, MOV_IZQUIERDA, lista_sucesores)

    return lista_sucesores

def mostrar_info_sucesores(estado: estado_nivel.EstadoNivel):
    """
    Nombre de la función: mostrar_info_sucesores

    Descripción de la función: Muestra la información de los sucesores de un estado dado de un nivel

    Parámetros de entrada:
        estado (estado_nivel.EstadoNivel): Representa el estado actual del nivel
    """

    estado.actualizar_id_nivel()
    sucesores_validos = funcion_sucesores(estado)
    print(f"ID:{estado.id_nivel}")

    for sucesor in sucesores_validos:
        print(f"\t[{sucesor[0]},{sucesor[1].id_nivel},{sucesor[2]}]")
