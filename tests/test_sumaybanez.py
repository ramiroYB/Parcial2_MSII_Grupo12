from funciones.sumaybanez import sumar

def test_sumar():
    assert sumar(3, 5) == 8
    assert sumar(-2, 2) == 0
    assert sumar(10, 10) == 20