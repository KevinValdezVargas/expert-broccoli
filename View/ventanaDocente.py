from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoDocente import *

aDoc = arregloDocente()

class ventanaDocente(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaDocente, self).__init__(parent)
        uic.loadUi("UI/ventanaDocente.ui", self)
        # self.btnListar.clicked.connect(self.ListarDatos)
        self.listar()
        self.show()

    def listar(self):
        self.tblDocentes.setRowCount(aDoc.tamañoArregloDocente())
        self.tblDocentes.setColumnCount(5)
        self.tblDocentes.verticalHeader().setVisible(False)

        for i in range(0, aDoc.tamañoArregloDocente()):
            self.tblDocentes.setItem(i, 0, QtWidgets.QTableWidgetItem(aDoc.devolverDocente(i).getCodigo()))
            self.tblDocentes.setItem(i, 1, QtWidgets.QTableWidgetItem(aDoc.devolverDocente(i).getNombres()))
            self.tblDocentes.setItem(i, 2, QtWidgets.QTableWidgetItem(aDoc.devolverDocente(i).getApellidos()))
            self.tblDocentes.setItem(i, 3, QtWidgets.QTableWidgetItem(aDoc.devolverDocente(i).getDni()))
            self.tblDocentes.setItem(i, 4, QtWidgets.QTableWidgetItem(aDoc.devolverDocente(i).getGradoAcademico()))
