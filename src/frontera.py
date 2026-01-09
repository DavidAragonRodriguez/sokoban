#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: frontera.py                                       #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 04/11/2024                                         #
# Descripción del fichero: El módulo principal de este archivo es la    #
# clase Frontera, que almacena toda la información de la frontera de    #
# nuestro problema. Además, permite comprobar si está vacía, añadir un  #
# nuevo nodo (empleando inserción ordenada) y extraer el primer nodo.   #
#                                                                       #
#########################################################################

"""
Importamos la librería necesaria para la inserción ordenada y
el módulo necesario para almacenar los nodos de la frontera
"""
import heapq

import nodo

class Frontera:
    """
    Nombre de la clase: Frontera

    Fecha de creación: 04/11/2024

    Descripción de la clase: Clase que almacena los nodos de la frontera
    """

    def __init__(self):
        """
        Nombre del método: __init__

        Descripción del método: Constructor de la clase Frontera
        """

        self.nodos_frontera = []

    def hay_nodos(self) -> bool:
        """
        Nombre del método: hay_nodos

        Descripción del método: Comprueba si hay nodos en la frontera

        Valores de retorno:
            bool: Indica si hay nodos (TRUE) o no (FALSE)
        """

        return len(self.nodos_frontera) > 0

    def insertar(self, nodo_entrada: nodo.Nodo) -> None:
        """
        Nombre del método: insertar

        Descripción del método: Añade mediante inserción ordenada un nodo a la frontera

        Parámetros de entrada:
            nodo_entrada (nodo.Nodo): Nodo a añadir a la frontera
        """

        heapq.heappush(self.nodos_frontera, nodo_entrada)

    def extraer(self) -> nodo.Nodo:
        """
        Nombre del método: extraer

        Descripción del método: Extrae el primer nodo de la frontera

        Valores de retorno:
            nodo.Nodo: El nodo extraído de la frontera
        """

        nodo_extraido = None

        if self.hay_nodos():
            nodo_extraido = heapq.heappop(self.nodos_frontera)

        return nodo_extraido
