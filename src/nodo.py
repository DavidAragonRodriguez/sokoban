#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: nodo.py                                           #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 04/11/2024                                         #
# Descripción del fichero: El módulo principal de este archivo es la    #
# clase Nodo, que almacena toda la información del nodo de nuestro      #
# problema. Además, permite obtener el camino hasta llegar a él,        #
# mostrar su información con el formato que se nos pide y definir un    #
# método similar a un 'compareTo' para ordenar los nodos por valor y,   #
# en caso de empate, por id (de menora mayor).                          #
#                                                                       #
#########################################################################

class Nodo:
    """
    Nombre de la clase: Nodo

    Fecha de creación: 04/11/2024

    Descripción de la clase: Clase que almacena toda la información de un nodo del árbol de búsqueda
    """

    id_cont = 0     # Atributo de clase que se incrementa cada vez que se crea una instancia 'Nodo'

    def __init__(self, info_nodo: tuple, padre: 'Nodo'):
        """
        Nombre del método: __init__

        Descripción del método: Constructor de la clase Nodo

        Parámetros de entrada:
            info_nodo (tuple): Tupla (accion, estado, coste_accion):
                accion: acción que ha generado el estado almacenado
                estado: estado que almacena el nodo
                coste_accion: coste de la acción que ha generado el estado almacenado
            padre ('Nodo'): Nodo padre del nodo actual
        """

        self.id = Nodo.id_cont
        Nodo.id_cont += 1

        self.accion = info_nodo[0]
        self.estado = info_nodo[1]
        self.padre = padre
        self.valor = 0.00

        if padre is None:
            self.profundidad = 0
            self.costo = 0.00

        else:
            self.profundidad = padre.profundidad + 1
            self.costo = padre.costo + 1.00

    def obtener_camino(self) -> list:
        """
        Nombre del método: obtener_camino

        Descripción del método: Método que obtiene el camino hasta llegar al nodo actual

        Valores de retorno:
            list: Nodos ordenados desde el nodo inicial hasta el actual (self)
        """

        nodo_actual = self
        camino = []

        while nodo_actual.padre is not None:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre

        camino.append(nodo_actual)
        camino.reverse()

        return camino

    def info_nodo(self) -> str:
        """
        Nombre del método: info_nodo

        Descripción del método: Método que muestra la información del nodo siguiendo el
        formato especificado

        Valores de retorno:
            str: Cadena con toda la información del nodo con el formato correcto
        """

        self.valor = int(self.valor * 100 + 0.5) / 100

        if self.padre is None:
            id_padre = None

        else:
            id_padre = self.padre.id

        return (f"{self.id},{self.estado.id_nivel},{id_padre},"
                f"{self.accion},{self.profundidad},{self.costo:.2f},"
                f"{self.estado.heuristica:.2f},{self.valor:.2f}")

    def __lt__(self, otro_nodo: 'Nodo') -> bool:
        """
        Nombre del método: __lt__

        Descripción del método: Comparar el nodo self con otro nodo para su ordenación

        Parámetros de entrada:
            otro_nodo ('Nodo'): Nodo a comparar con el actual

        Valores de retorno:
            bool: Devuelve TRUE si el valor del nodo self es menor y FALSE si el valor del otro
            nodo es menor (en caso de empate, devuelve TRUE si el id del nodo self es menor y
            FALSE si el id del otro nodo es menor)
        """

        if self.valor == otro_nodo.valor:
            return self.id < otro_nodo.id

        return self.valor < otro_nodo.valor
