#!/usr/bin/env python3

#########################################################################
#                                                                       #
# Nombre del fichero: estado_nivel.py                                   #
# Nombre del autor: David Aragón Rodríguez (grupo B1)                   #
# DNI del autor: 71374640M                                              #
# Fecha de creación: 01/10/2024                                         #
# Descripción del fichero: El módulo principal de este archivo es la    #
# clase EstadoNivel, que almacena toda la información de un nivel del   #
# Sokoban. Además, utiliza funciones externas para calcular los         #
# elementos de dicho nivel.                                             #
#                                                                       #
#########################################################################

""" Importamos el módulo necesario para usar las funciones que calculen los elementos del nivel """
import funciones

from constantes import MURO, JUGADOR, CAJA, CAJA_EN_OBJETIVO, OBJETIVO, JUGADOR_EN_OBJETIVO
from constantes import TRUE_STR, FALSE_STR

class EstadoNivel:
    """
    Nombre de la clase: EstadoNivel

    Fecha de creación: 01/10/2024

    Descripción de la clase: Clase que almacena toda la información de un nivel o estado
    """

    def __init__(self, nivel: str):
        """
        Nombre del método: __init__

        Descripción del método: Constructor de la clase EstadoNivel

        Parámetros de entrada:
            nivel (str): Nivel del sokoban que representa el estado actual
        """

        self.nivel = nivel
        self.filas = None
        self.columnas = None
        self.lista_muros = []
        self.lista_objetivos = []
        self.lista_cajas = []
        self.pos_jugador = None
        self.id_nivel = ""
        self.heuristica = 0.00

        self.calcular_elementos_nivel()

    def calcular_elementos_nivel(self):
        """
        Nombre del método: calcular_elementos_nivel

        Descripción del método: Se llama al crear una instancia de EstadoNivel
        para darle valores a sus atributos
        """

        self.filas, self.columnas = funciones.calcular_filas_columnas(self.nivel)

        filas_nivel = self.nivel.split('\\n')
        num_fila = 0

        for fila in filas_nivel:

            num_columna = 0

            for columna in fila:

                if columna == MURO:
                    self.lista_muros.append((num_fila,num_columna))
                elif columna == JUGADOR:
                    self.pos_jugador = (num_fila,num_columna)
                elif columna == CAJA:
                    self.lista_cajas.append((num_fila,num_columna))
                elif columna == OBJETIVO:
                    self.lista_objetivos.append((num_fila,num_columna))
                elif columna == CAJA_EN_OBJETIVO:
                    self.lista_cajas.append((num_fila,num_columna))
                    self.lista_objetivos.append((num_fila,num_columna))
                elif columna == JUGADOR_EN_OBJETIVO:
                    self.pos_jugador = (num_fila,num_columna)
                    self.lista_objetivos.append((num_fila,num_columna))

                num_columna += 1

            num_fila += 1

        self.actualizar_id_nivel()

    def actualizar_id_nivel(self):
        """
        Nombre del método: actualizar_id_nivel

        Descripción del método: Actualiza el id del nivel por si se han modificado
        las posiciones del jugador o de alguna de las cajas
        """
        self.id_nivel = funciones.calcular_id(self.pos_jugador, self.lista_cajas)

    def mostrar_info_nivel(self):
        """
        Nombre del método: mostrar_info_nivel

        Descripción del método: Muestra toda la información del estado o nivel que lo invoca
        """

        print(f"ID:{self.id_nivel}")
        print(f"\tRows:{self.filas}")
        print(f"\tColumns:{self.columnas}")
        print(f"\tWalls:[{funciones.formatear_lista(self.lista_muros)}]")
        print(f"\tTargets:[{funciones.formatear_lista(self.lista_objetivos)}]")
        print(f"\tPlayer:({self.pos_jugador[0]},{self.pos_jugador[1]})")
        print(f"\tBoxes:[{funciones.formatear_lista(self.lista_cajas)}]")

    def funcion_objetivo(self) -> str:
        """
        Nombre del método: funcion_objetivo

        Descripción del método: Aplica la función objetivo al estado para comprobar si es solución

        Valores de retorno:
            str: Indica si el estado es objetivo (TRUE) o no (FALSE)
        """
        es_objetivo = TRUE_STR

        self.lista_cajas.sort()
        self.lista_objetivos.sort()

        for caja in self.lista_cajas:
            if caja not in self.lista_objetivos:
                es_objetivo = FALSE_STR

        return es_objetivo

    def funcion_heuristica(self) -> float:
        """
        Nombre del método: funcion_heuristica

        Descripción del método: Aplica la función heurística al estado para calcular su valor
        usando la distancia de Manhattan

        Valores de retorno:
            float: Valor de la función heurística
        """

        heuristica = 0.00
        d_manhattan_caja = -1.00
        d_manhattan_provisional = -1.00

        for caja in self.lista_cajas:

            for objetivo in self.lista_objetivos:

                d_manhattan_provisional = abs(objetivo[0] - caja[0]) + abs(objetivo[1] - caja[1])

                if d_manhattan_provisional < d_manhattan_caja or d_manhattan_caja == -1.00:
                    d_manhattan_caja = d_manhattan_provisional

            heuristica += d_manhattan_caja
            d_manhattan_caja = -1.00

        self.heuristica = heuristica

        return heuristica
