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
    calculadora1 = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora1.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora1.resta(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calculadora1.mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = calculadora1.div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide.')

    print("The result of", operando1, sys.argv[2], operando2, "is", result)
