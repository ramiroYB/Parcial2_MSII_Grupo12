from funciones.dividir_jose_Grabiel import dividir_jose_Grabiel

def test_dividir():
    assert dividir_jose_Grabiel(10, 2) == 5
    assert dividir_jose_Grabiel(5, 0) is None
