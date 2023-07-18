from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoEspecialidad import *

aCli = mantenimientoEspecialidad()

class ventanaEspecialidad(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaEspecialidad,self).__init__(parent)
        uic.loadUi("",self)
        self.show()