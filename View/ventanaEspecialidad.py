from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoEspecialidad import *

aEspe = arregloEspecialidad()

class ventanaEspecialidad(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaEspecialidad,self).__init__(parent)
        uic.loadUi("UI/ventanaEspecialidad.ui",self)
        # self.btnListar.clicked.connect(self.ListarDatos)
        self.listar()
        self.show()

    def listar(self):
        self.tblEspecialidad.setRowCount(aEspe.tamañoArregloEspecialidad())
        self.tblEspecialidad.setColumnCount(4)
        self.tblEspecialidad.verticalHeader().setVisible(False)

        for i in range(0, aEspe.tamañoArregloEspecialidad()):
            self.tblEspecialidad.setItem(i, 0, QtWidgets.QTableWidgetItem(aEspe.devolverEspecialidad(i).getCodigo()))
            self.tblEspecialidad.setItem(i, 1, QtWidgets.QTableWidgetItem(aEspe.devolverEspecialidad(i).getNombre()))
            self.tblEspecialidad.setItem(i, 2, QtWidgets.QTableWidgetItem(aEspe.devolverEspecialidad(i).getCreditos()))
            self.tblEspecialidad.setItem(i, 3, QtWidgets.QTableWidgetItem(aEspe.devolverEspecialidad(i).getResolucion()))