#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    def suma(self, operador1, operador2):
        return (operador1 + operador2)

    def resta(self, operador1, operador2):
        return (operador1 - operador2)

class CalculadoraHija(Calculadora):
    def mult(self, operador1, operador2):
        return(operador1 * operador2)

    def div(self, operador1, operador2):
        try:
            return(operador1 / operador2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
