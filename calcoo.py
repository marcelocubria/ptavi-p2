#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def suma(self, operador1, operador2):
        return (operador1 + operador2)

    def resta(self, operador1, operador2):
        return (operador1 - operador2)


if __name__ == "__main__":
    try:
        calculadora1 = Calculadora()
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora1.suma(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "resta":
        result = calculadora1.resta(int(sys.argv[1]), int(sys.argv[3]))
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print("The result of", sys.argv[1], sys.argv[2], sys.argv[3], "is", result)
