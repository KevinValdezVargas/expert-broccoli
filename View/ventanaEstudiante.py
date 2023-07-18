from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoEstudiante import *

aEst = mantenimientoEstudiante()

class ventanaEstudiante(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaEstudiante,self).__init__(parent)
        uic.loadUi("UI/ventanaEstudiante.ui",self)
        self.show()