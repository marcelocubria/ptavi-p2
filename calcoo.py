#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2

    def suma(self):
        return (self.operador1 + self.operador2)

    def resta(self):
        return (self.operador1 - self.operador2)

if __name__ == "__main__":
    try:
        calculadora1 = Calculadora(int(sys.argv[1]), int(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora1.suma();
    elif sys.argv[2] == "resta":
        result = calculadora1.resta();
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print("El resultado de", sys.argv[1], sys.argv[2], int(sys.argv[3]), "es igual a", result)
