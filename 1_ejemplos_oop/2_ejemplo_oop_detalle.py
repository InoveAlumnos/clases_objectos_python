#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos para contrastar
contra la programamación procedural
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


class Animal():
    '''Clase base Animal'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        if self.age > 1:
            return 12
        else:
            return 16

    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    '''Clase Dog que hereda de Animal'''
    def sleep(self):
        if self.age > 1:
            return 8
        else:
            return 16

    def speak(self):
        print('Dog say: Guau!')


class Cat(Animal):
    '''Clase Cat que hereda de Animal'''
    def sleep(self):
        if self.age > 1:
            return 10
        else:
            return 18

    def speak(self):
        print('Cat say: Miau!')


# class Cow(Animal):
#     ''' Clase Cow que hereda de Animal'''
#     def __init__(self, name, age, tipo):
#         super().__init__(name, age)
#         self.type = tipo

#     def sleep(self):
#         if self.age > 3:
#             if self.type == 'milk':
#                 return 10
#             else:
#                 return 4
#         else:
#             return 10


class Person():
    ''' Clase persona'''
    def __init__(self, name):
        self.name = name
        self.animales = []

    def adopt(self, animal):
        self.animales.append(animal)


if __name__ == '__main__':

    animal_1 = Dog('Sirius', 8)
    animal_2 = Cat('Minerva', 1)

    #animal_3 = Cow("milka", 4, "milk")
    #animal_3.speak()

    print('¿Cuanto duerme el perro por la noche?', animal_1.sleep())
    print('¿Cuanto duerme el gato por la noche?', animal_2.sleep())

    persona = Person('Max')
    print('{} adoptó 2 animales, un perro y un gato'.format(persona.name))

    persona.adopt(animal_1)
    persona.adopt(animal_2)

    print('¿Cómo saludan los animales de', persona.name, '?')

    for animal in persona.animales:
        animal.speak()
