#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora


class CalculadoraHija(Calculadora):
    def mult(self, operador1, operador2):
        return(operador1 * operador2)

    def div(self, operador1, operador2):
        try:
            return(operador1 / operador2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")


if __name__ == "__main__":
    try:
        calculadora1 = CalculadoraHija()
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora1.suma(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "resta":
        result = calculadora1.resta(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "multiplicacion":
        result = calculadora1.mult(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "division":
        result = calculadora1.div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print("The result of", sys.argv[1], sys.argv[2], sys.argv[3], "is", result)
