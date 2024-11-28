#Clase de rotación

import numpy as np
from .Vector3D import Trivector

class Rotacion:
    def __init__(self, angle, axis):
        """
        Inicializa una rotación 3D dado un ángulo y un eje de rotación.
        :param angle: Ángulo de rotación en radianes.
        :param axis: Eje de rotación como un trivector.
        """
        if not isinstance(axis, Trivector):
            raise ValueError("El eje debe ser un Trivector")
        
        # Normaliza el eje de rotación
        norm = np.linalg.norm(axis.vector)
        if norm == 0:
            raise ValueError("El eje de rotación no puede ser el vector cero")
        
        axis_normalized = axis.vector / norm
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)

        # Matriz de rotación utilizando la fórmula de Rodrigues
        self.rotation_matrix = np.array([
            [cos_a + axis_normalized[0]**2 * (1 - cos_a),
             axis_normalized[0] * axis_normalized[1] * (1 - cos_a) - axis_normalized[2] * sin_a,
             axis_normalized[0] * axis_normalized[2] * (1 - cos_a) + axis_normalized[1] * sin_a],

            [axis_normalized[1] * axis_normalized[0] * (1 - cos_a) + axis_normalized[2] * sin_a,
             cos_a + axis_normalized[1]**2 * (1 - cos_a),
             axis_normalized[1] * axis_normalized[2] * (1 - cos_a) - axis_normalized[0] * sin_a],

            [axis_normalized[2] * axis_normalized[0] * (1 - cos_a) - axis_normalized[1] * sin_a,
             axis_normalized[2] * axis_normalized[1] * (1 - cos_a) + axis_normalized[0] * sin_a,
             cos_a + axis_normalized[2]**2 * (1 - cos_a)]
        ], dtype=complex)

    def apply(self, vector):
        """Aplica la rotación al Trivector dado."""
        if not isinstance(vector, Trivector):
            raise ValueError("El vector debe ser una instancia de Trivector")
        rotated_vector = self.rotation_matrix @ vector.vector
        return Trivector(*rotated_vector)

    def __repr__(self):
        return f"Rotación resultante: (rotation_matrix=\n{self.rotation_matrix})"





