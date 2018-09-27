#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def suma(self, operador1, operador2):
        return (operador1 + operador2)

    def resta(self, operador1, operador2):
        return (operador1 - operador2)


if __name__ == "__main__":
    calculadora1 = Calculadora()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora1.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora1.resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print("The result of", operando1, sys.argv[2], operando2, "is", result)
