from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from View.ventanaDocente import ventanaDocente
from View.ventanaEspecialidad import ventanaEspecialidad

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui", self)
        self.show()

    # Procesos
        self.actionDocente.triggered.connect(self.abrirVentanaDocente)
        self.actionEspecialidad.triggered.connect(self.abrirVentanaEspecialidad)

    def abrirVentanaDocente(self):
        vDocente = ventanaDocente(self)
        vDocente.show()

    def abrirVentanaEspecialidad(self):
        vEspecialidad = ventanaEspecialidad(self)
        vEspecialidad.show()

    def cerrar(self):
        self.close()