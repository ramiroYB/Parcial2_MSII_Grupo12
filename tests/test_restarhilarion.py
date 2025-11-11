# tests/test_restarhilarion.py

# Importa la función 'restar' desde el módulo 'funciones.restarhilarion'
from funciones.restarhilarion import restar

def test_restarhilarion():
    assert restar(10, 4) == 6
    assert restar(5, 10) == -5