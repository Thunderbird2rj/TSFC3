# First_Package/gui.py

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from First_Package import Vector3D, Particulas, Rotacion, Cuadrivector
import sys
import numpy as np

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Aplicación de Ejemplo - First_Package")
        self.setGeometry(100, 100, 400, 300)
        
        # Layout
        layout = QVBoxLayout()
        
        # Etiqueta de instrucciones
        self.instruction_label = QLabel("Elige una función para ejecutar:")
        layout.addWidget(self.instruction_label)
        
        # Botón para ejemplo de Trivector
        self.button1 = QPushButton("Mostrar Trivector")
        self.button1.clicked.connect(self.show_trivector)
        layout.addWidget(self.button1)
        
        # Botón para ejemplo de Particula
        self.button2 = QPushButton("Mostrar Particula")
        self.button2.clicked.connect(self.show_particula)
        layout.addWidget(self.button2)
        
        # Botón para ejemplo de Rotacion
        self.button3 = QPushButton("Mostrar Rotacion")
        self.button3.clicked.connect(self.show_rotacion)
        layout.addWidget(self.button3)
        
        # Botón para ejemplo de Cuadrivector
        self.button4 = QPushButton("Mostrar Cuadrivector")
        self.button4.clicked.connect(self.show_cuadrivector)
        layout.addWidget(self.button4)
        
        # Etiqueta para mostrar el resultado
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        
        # Configurar el layout principal
        self.setLayout(layout)

    def show_trivector(self):
        # Crear y mostrar un Trivector
        trivector = Vector3D.Trivector(1.0, 2.0, 3.0)
        self.result_label.setText(trivector.__resul__())

    def show_particula(self):
        # Crear y mostrar una Particula
        particula = Particulas.Lepton1(
        nombre='Electron',
        masa="0.51099895000±0.00000000015",
        carga=-1,
        mommag="(1159.65218062±0.00000012)e-6",
        vm='>6.6e-28 años',
        logn_de_des="-",
        dipolo_electrico='<0.041e-28',
        dipolo_debil='-',
        neutrinos=3,
        anomalia='-',
        familia_leptonica='-'
    )
        self.result_label.setText(particula.info())

        
    def show_rotacion(self):
        # Crear y mostrar una Rotacion aplicada a un Trivector
        trivector = Vector3D.Trivector(1.0, 0.0, 0.0)
        rotacion = Rotacion.Rotacion(np.pi/4, Vector3D.Trivector(0.0, 0.0, 1.0))
        rotated_trivector = rotacion.apply(trivector)
        self.result_label.setText(rotated_trivector.__resul__())

    def show_cuadrivector(self):
        # Crear y mostrar un Cuadrivector
        cuadrivector = Cuadrivector.Cuadrivector(1.0, 2.0, 3.0, 4.0)
        self.result_label.setText(str(cuadrivector))

def main():
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
