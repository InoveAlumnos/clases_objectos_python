#!/usr/bin/env python
'''
Test finanzas [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba finanzas.py
'''

import unittest
from finanzas import *

class FinanzasTestCase(unittest.TestCase):
    ''' Ensayo de las APIs de meli'''
    def test_instrument(self):
        # crear un bono
        bond = Bond('USA10Y')

        # Comprar 10 bonos a 0.5
        bond.append_transaction(trans_type='BUY', unit_price=0.5, quantity=10)
        # Comprar 10 bonos a 0.5
        bond.append_transaction(trans_type='BUY', unit_price=0.5, quantity=10)

        # Calcular el valor esperado de la inversion hecha hasta el momento
        valor_esperado = 10 * 0.5 + 10 * 0.5

        # Verificar si en el objecto se posee la misma información (Equal)
        self.assertEqual(bond.sum_quantity_unit_price, valor_esperado)

    def test_pnl(self):
        # crear un bono
        bond = Bond('USA10Y')

        # Comprar 10 bonos a 0.5
        bond.append_transaction(trans_type='BUY', unit_price=0.5, quantity=10)
        # Comprar 10 bonos a 0.5
        bond.append_transaction(trans_type='BUY', unit_price=0.5, quantity=10)

        # Calcular el valor esperado de ganancia
        precio_actual = bond.get_price()
        valor_esperado = 20 * (precio_actual - 0.5)

        # Verificar si el objecto posee la misma información (Equal)
        self.assertEqual(bond.pnl(), valor_esperado)


if __name__ == '__main__':
    unittest.main()
