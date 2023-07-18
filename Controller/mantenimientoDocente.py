from Controller.controllerDocente import *

class arregloDocente:

    def __init__(self):
        self.dataDocentes = []
        self.cargar()

    def adicionaDocente(self, objDoc):
        self.dataDocentes.append(objDoc)

    def devolverDocente(self, pos):
        return self.dataDocentes[pos]
    def tamañoArregloDocente(self):
        return len(self.dataDocentes)
    def cargar(self):
        archivo = open("Model/docentes.txt", "r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0].strip()
            nombres = columna[1].strip()
            apellidos = columna[2].strip()
            dni = columna[3].strip()
            gradoAcademico = columna[4].strip()
            objDoc = Producto(codigo, nombres, apellidos, dni, gradoAcademico)
            self.adicionaDocente(objDoc)
        archivo.close()