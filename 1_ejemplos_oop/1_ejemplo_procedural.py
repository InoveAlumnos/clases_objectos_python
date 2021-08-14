#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos para contrastar
contra la programamación orientada a objectos
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def sleep(animal, age):
    if animal == 'Dog':
        if age > 1:
            return 8
        else:
            return 16
    elif animal == 'Cat':
        if age > 1:
            return 10
        else:
            return 18
    elif animal == 'Cow':
        if age > 3:
            return 4
        else:
            return 10
    else:
        print('Animal not found')
        return 0


def speak(animal):
    if animal == 'Dog':
        print('Dog say: Guau!')
    elif animal == 'Cat':
        print('Cat say: Miau!')
    elif animal == 'Cow':
        print('Cow say: Muuu!')
    else:
        print('Animal not found')


if __name__ == '__main__':

    animal_1 = 'Dog'
    animal_1_nombre = 'Sirius'
    animal_1_edad = 8

    animal_2 = 'Cat'
    animal_2_nombre = 'Minerva'
    animal_2_edad = 1

    print('¿Cuanto duerme el perro por la noche?', sleep(animal_1, animal_1_edad))
    print('¿Cuanto duerme el gato por la noche?', sleep(animal_2, animal_2_edad))

    persona_nombre = 'Max'
    print('{} adoptó 2 animales, un perro y un gato'.format(persona_nombre))

    persona_animales = []

    animal_adoptado_1 = {'tipo': animal_1, 'nombre': animal_1_nombre, 'edad': animal_1_edad}
    persona_animales.append(animal_adoptado_1)

    animal_adoptado_2 = {'tipo': animal_2, 'nombre': animal_2_nombre, 'edad': animal_2_edad}
    persona_animales.append(animal_adoptado_2)

    print('¿Cómo saludan los animales de', persona_nombre, '?')

    for animal in persona_animales:
        speak(animal['tipo'])
