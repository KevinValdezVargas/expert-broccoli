from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
from Controller.mantenimientoEstudiante import *

aEst = arregloEstudiante()

class ventanaEstudiante(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(ventanaEstudiante,self).__init__(parent)
        uic.loadUi("UI/ventanaEstudiante.ui",self)
        #self.btnListar.clicked.connect(self.ListarDatos)
        #self.ListarDatos()
        self.show()

    #Procesos
    def ListarDatos(self):
        self.tblEstudiante.setRowCount(aEst.tamañoArregloEstudiante())
        self.tblEstudiante.setColumnCount(6)
        self.tblEstudiante.verticalHeader().setVisible(False)

        for i in range(0, aEst.tamañoArregloEstudiante()):
            self.tblEstudiante.setItem(i,0,QtWidgets.QTableWidgetItem(aEst.devolverEstudiante(i).getCodigo()))
            self.tblEstudiante.setItem(i,1,QtWidgets.QTableWidgetItem(aEst.devolverEstudiante(i).getNombres()))
            self.tblEstudiante.setItem(i,2,QtWidgets.QTableWidgetItem(aEst.devolverEstudiante(i).getApellidos()))
            self.tblEstudiante.setItem(i,3,QtWidgets.QTableWidgetItem(aEst.devolverEstudiante(i).getCiclo()))
            self.tblEstudiante.setItem(i,4,QtWidgets.QTableWidgetItem(aEst.devolverEstudiante(i).getEspecialidad()))