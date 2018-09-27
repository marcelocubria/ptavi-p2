#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calculadorahija import CalculadoraHija


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
        sys.exit('Operación sólo puede ser sumar o restar.')

    print("The result of", operando1, sys.argv[2], operando2, "is", result)
