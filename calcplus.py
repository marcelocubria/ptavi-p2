#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija


if __name__ == "__main__":
    nombre_fichero = sys.argv[1]
    fichero = open(nombre_fichero)
    calculadora1 = CalculadoraHija();

    for line in fichero.readlines():
        operacion_valores = line.split(',')
        acumulador = int(operacion_valores[1])
        if operacion_valores[0] == "suma":
            for valor in operacion_valores[2:]:
                acumulador = calculadora1.suma(acumulador, int(valor))
        elif operacion_valores[0] == "resta":
            for valor in operacion_valores[2:]:
                acumulador = calculadora1.resta(acumulador, int(valor))
        elif operacion_valores[0] == "multiplica":
            for valor in operacion_valores[2:]:
                acumulador = calculadora1.mult(acumulador, int(valor))
        elif operacion_valores[0] == "divide":
            for valor in operacion_valores[2:]:
                acumulador = calculadora1.div(acumulador, int(valor))
        print(acumulador)