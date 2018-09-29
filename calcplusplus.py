#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
from calculadorahija import CalculadoraHija


if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as csvfile:
            lector = csv.reader(csvfile)
            calc1 = CalculadoraHija()
            for line in lector:
                acumulador = int(line[1])
                if line[0] == "suma":
                    try:
                        for valor in line[2:]:
                            acumulador = calc1.suma(acumulador, int(valor))
                        print(acumulador)
                    except ValueError:
                        print("Un valor en la suma no es valido")
                elif line[0] == "resta":
                    try:
                        for valor in line[2:]:
                            acumulador = calc1.resta(acumulador, int(valor))
                        print(acumulador)
                    except ValueError:
                        print("Un valor en la resta no es valido")
                elif line[0] == "multiplica":
                    try:
                        for valor in line[2:]:
                            acumulador = calc1.mult(acumulador, int(valor))
                        print(acumulador)
                    except ValueError:
                        print("Un valor en la multiplicación no es valido")
                elif line[0] == "divide":
                    try:
                        for valor in line[2:]:
                            acumulador = calc1.div(acumulador, int(valor))
                        print(acumulador)
                    except ValueError:
                        print("Un valor en la división no es valido")
                else:
                    print("Operacion invalida")
    except IOError:
        sys.exit("No existe el fichero indicado")
