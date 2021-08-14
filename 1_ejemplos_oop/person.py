#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Modulo con Clase Person y sus derivados
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


class Person():
    '''Clase persona'''
    def __init__(self, name):
        self.name = name
        self.animales = []

    def adopt(self, animal):
        self.animales.append(animal)
