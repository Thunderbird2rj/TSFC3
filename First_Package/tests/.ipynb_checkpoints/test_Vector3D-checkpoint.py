# Importamos la clase Trivector
from First_Package.Vector3D import Trivector  

def test_inicializacion():
    v = Trivector(1, 2, 3)
    assert v.vector[0] == 1.0, f"Se esperaba 1.0, pero fue {v.vector[0]}"
    assert v.vector[1] == 2.0, f"Se esperaba 2.0, pero fue {v.vector[1]}"
    assert v.vector[2] == 3.0, f"Se esperaba 3.0, pero fue {v.vector[2]}"

def test_suma():
    v1 = Trivector(1, 2, 3)
    v2 = Trivector(4, 5, 6)
    v3 = v1.__suma__(v2)
    assert v3.vector[0] == 5.0, f"Se esperaba 5.0, pero fue {v3.vector[0]}"
    assert v3.vector[1] == 7.0, f"Se esperaba 7.0, pero fue {v3.vector[1]}"
    assert v3.vector[2] == 9.0, f"Se esperaba 9.0, pero fue {v3.vector[2]}"

def test_resta():
    v1 = Trivector(1, 2, 3)
    v2 = Trivector(4, 5, 6)
    v3 = v1.__resta__(v2)
    assert v3.vector[0] == -3.0, f"Se esperaba -3.0, pero fue {v3.vector[0]}"
    assert v3.vector[1] == -3.0, f"Se esperaba -3.0, pero fue {v3.vector[1]}"
    assert v3.vector[2] == -3.0, f"Se esperaba -3.0, pero fue {v3.vector[2]}"
    
def test_prod_escalar():
    v1 = Trivector(1, 2, 3)
    escalar = 2
    resultado = v1.__escalar__(escalar)
    assert resultado.vector[0] == 2.0, f"Se esperaba 2.0 pero fue {resultado.vector[0]}"
    assert resultado.vector[1] == 4.0, f"Se esperaba 4.0 pero fue {resultado.vector[0]}"
    assert resultado.vector[2] == 6.0, f"Se esperaba 6.0 pero fue {resultado.vector[0]}"

def test_producto_punto():
    v1 = Trivector(1, 2, 3)
    v2 = Trivector(4, 5, 6)
    resultado = v1.punto(v2)
    assert resultado == 32, f"Se eperaba 32, pero fue {resultado}"

def test_producto_cruz():
    v1 = Trivector(1, 2, 3)
    v2 = Trivector(4, 5, 6)
    v3 = v1.cruz(v2)
    assert v3.vector[0] == -3.0, f"Se esperaba -3.0, pero fue {v3.vector[0]}"
    assert v3.vector[1] == 6.0, f"Se esperaba 6.0, pero fue {v3.vector[1]}"
    assert v3.vector[2] == -3.0, f"Se esperaba -3.0, pero fue {v3.vector[2]}"

def test_resul():
    v = Trivector(1, 2, 3)
    resultado = v.__resul__()
    esperado = "Coordenadas del vector resultante(x=(1+0j), y=(2+0j), z=(3+0j))"
    assert resultado == esperado, f"Se esperaba: {esperado}, pero fue: {resultado}"

# Ejecutamos todos los tests
def run_tests():
    test_inicializacion()
    test_suma()
    test_resta()
    test_prod_escalar()
    test_producto_punto()
    test_producto_cruz()
    test_resul()

