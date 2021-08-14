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


class Instrument():
    '''Instrument base clase
        Un instrumento finanziero puede ser:
        - Bonos (bond)
        - Acciones (stock)
        - Dinero (cash)
    
    Esta clase por cada instrumento que posea la persona (porfolio)
    almacena la cantidad y el valor total de ese instrumento

    '''
    _factory_registry = {}  # Registered subclasses

    def __init__(self, name):
        self.name = name
        self.sum_quantity_unit_price = 0.0
        self.sum_quantity = 0

    def append_transaction(self, trans_type, unit_price, quantity):
        # Save transaction for future implementation

        # Si la transaccion a efectuar es compra
        # debo aumentar las unidades de ese instrumento
        # y el valor de compra
        if trans_type == 'BUY':
            self.sum_quantity += quantity
            self.sum_quantity_unit_price += quantity * unit_price
        else:
            self.sum_quantity -= quantity
            self.sum_quantity_unit_price -= quantity * unit_price

    def current_value(self):
        # Retorna el valor de mi instrumento, considerado
        # el precio vigente y la cantidad comprados
        current_price = self.get_price()
        return self.sum_quantity * current_price

    def pnl(self):
        # Retorna la pérdida o ganancia de mi instrumento
        current_price = self.get_price()
        purchase_price = self.sum_quantity_unit_price / self.sum_quantity
        return self.sum_quantity * (current_price - purchase_price)

    def get_price(self):
        # Virtual method
        raise NotImplementedError


class Bond(Instrument):
    '''Bond generic class'''
    def get_price(self):
        # Acá podría utilizarse una API para obtener el valor
        # del bono en ese momento
        return 1.0


class Stock(Instrument):
    '''Stock generic class'''
    def get_price(self):
        # Acá podría utilizarse una API para obtener el valor
        # de la acción en ese momento
        return 364.50


class Cash(Instrument):
    '''Cash generic class'''

    def get_price(self):
        # Acá podría utilizarse una API para obtener el valor
        # de la moneda respecto al dolar en ese momento
        return 1.12


if __name__ == '__main__':
    # Crear un objecto para las acciones de Apple
    accion_apple = Stock('AAPLC')

    # Comprar 3 acciones a 350
    accion_apple.append_transaction(trans_type='BUY', unit_price=350, quantity=3)

    # Cantidad de acciones que compramos:
    print("Cantidad de acciones adquiridas:", accion_apple.sum_quantity)

    # El valor total invertido en esas acciones
    print("Inversión hasta el momento en acciones de Apple:", accion_apple.sum_quantity_unit_price)

    # Ver nuestro capital en acciones de Apple según el precio actual
    print("Valor actual de nuestras acciones:", accion_apple.current_value())

    # Ganancia hasta el momento
    print("Ganancia:", accion_apple.pnl())