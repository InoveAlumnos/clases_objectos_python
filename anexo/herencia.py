#!/usr/bin/env python
'''
Programación orientada a objectos [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

'''


class MyClass:
    """Ejemplo de una clase básica"""
    i = 12345  # atributo estático

    def speak(self):  # método
        return 'hello world'


class Herencia(MyClass):
    """Ejemplo de una herencia"""

    def speak(self):  # método
        return 'hola mundo'


class MyClass2:
    """Ejemplo de una clase básica"""
    i = 12345  # atributo estático

    def __init__(self, nombre=''):
        self.name = nombre
        self.number = 5

    def speak(self):  # método
        # Utilizo self para acceder al atributo de esta instancia
        name = self.name
        return '{}: hello world'.format(name)

    @staticmethod
    def author():
        print('Autor de esta clase: Inove Escuela de Código')

    @classmethod
    def set_i(cls, number):    # Método class que modifica i
        cls.i = number


class Herencia2(MyClass2):
    """Ejemplo de una herencia"""
    def __init__(self):
        super().__init__('ClaseHeredada')

    def speak(self):  # método
        return 'hola mundo'


if __name__ == '__main__':
    # Una variable estática existe aún antes de instanciar un objeto
    print(MyClass.i)
    MyClass.i = 10

    # Instancio dos objetos
    c1 = MyClass()
    c2 = Herencia()  # "Herencia" hereda "i" de "MyClass"

    # ¿Cuánto vale i en cada instancia?
    MyClass.i = 25
    print('c1.i=', c1.i)
    print('c2.i=', c2.i)

    # Polimorfismo
    print('c1:', c1.speak())  # Imprime 'hello world'
    print('c2:', c2.speak())  # Imprime 'hola mundo'

    c3 = MyClass2()    # Instancia objeto, llamar a constructor
    print(c3.name)     # Imprime ''
    print(c3.number)   # Imprime 5

    c4 = MyClass2('Max')  # Instancia objeto, llamar a constructor
    c4.number = 10     # Modificar el atributo number
    print(c4.name)     # Imprime 'Max'
    print(c4.number)   # Imprime 10
    print(c4.speak())  # Imprime 'Max: hello world'

    print(c3.number)   # Imprime 5

    MyClass2.author()  # Llamar al método estático author
    c4.author()        # Llamar al método estático author

    c5 = MyClass2('Jean')  # Instancia objeto, llamar a constructor
    print(c5.i)            # Visualizar valor de "i" antes de modificarlo
    # Modificar el valor de i para todos los objetos de la clase
    MyClass2.set_i(10) # El método como parámetro recibe el valor i deseado
    print(c4.i)        # Imprime 10
    print(c5.i)        # Imprime 10

    c6 = Herencia2()
    print(c6.name)
