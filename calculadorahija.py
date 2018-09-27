#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from calculadora import Calculadora


class CalculadoraHija(Calculadora):
    def mult(self, operador1, operador2):
        return(operador1 * operador2)

    def div(self, operador1, operador2):
        try:
            return(operador1 / operador2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
