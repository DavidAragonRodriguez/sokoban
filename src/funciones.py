#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: funciones.py                                      #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 09/10/2024                                         #
# Descripción del fichero: Contiene funciones útiles que se utilizarán  #
# en los otros ficheros del proyecto Sokoban.                           #
#                                                                       #
#########################################################################

""" Importamos la librería necesaria para la codificación MD5 """
import hashlib

def calcular_filas_columnas(nivel: str) -> tuple:
    """
    Nombre de la función: calcular_filas_columnas

    Descripción de la función: Calcula las filas y columnas del string
    que representa el nivel dado por el usuario

    Parámetros de entrada:
        nivel (str): Representa el nivel

    Valores de retorno:
        tuple: En número de filas y columnas del nivel
    """

    filas_nivel = nivel.split('\\n')
    n_filas = len(filas_nivel)

    n_columnas = 0

    for fila in filas_nivel:
        if n_columnas < len(fila):
            n_columnas = len(fila)

    return n_filas, n_columnas

def calcular_id(pos_jugador: tuple, lista_cajas: list) -> str:
    """
    Nombre de la función: calcular_id

    Descripción de la función: Obtención de la cadena que representa el ID
    y codificarla usando MD5

    Parámetros de entrada:
        pos_jugador (tuple): Contiene la posición (x, y) del jugador
        lista_cajas (list): Almacena las posiciones de las cajas

    Valores de retorno:
        str: ID del nivel en mayúsculas
    """

    pos_jugador_str = f"({pos_jugador[0]},{pos_jugador[1]})"

    lista_cajas_str = formatear_lista(lista_cajas)
    cajas_str = f"[{lista_cajas_str}]"

    id_str = f"{pos_jugador_str}{cajas_str}"

    id_bytes = id_str.encode("utf-8")
    id_hash = hashlib.md5(id_bytes)
    id_hash = id_hash.hexdigest()

    return id_hash.upper()

def formatear_lista(lista: list) -> str:
    """
    Nombre de la función: formatear_lista

    Descripción de la función: Devuelve los elementos de una lista
    separados por comas y sin espacios

    Parámetros de entrada:
        lista (list): Lista a formatear

    Valores de retorno:
        str: Los elementos de la lista con el formato adecuado para mostrarlos
    """

    lista_con_formato = []

    for elem in lista:
        lista_con_formato.append(f"({elem[0]},{elem[1]})")

    lista_str = ','.join(lista_con_formato)

    return lista_str
