#Clase para un vector tridimensional

import numpy as np

class Trivector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.vector = np.array([x, y, z], dtype=complex)

    def __suma__(self, other):
        return Trivector(*(self.vector + other.vector))

    def __resta__(self, other):
        return Trivector(*(self.vector - other.vector))

    def __escalar__(self, scalar):
        return Trivector(*(self.vector * scalar))

    def punto(self, other):
        return np.dot(self.vector, other.vector)

    def cruz(self, other):
        result = np.cross(self.vector, other.vector)
        return Trivector(*result)

    def __resul__(self):
        return f"Coordenadas del vector resultante(x={self.vector[0]}, y={self.vector[1]}, z={self.vector[2]})"





