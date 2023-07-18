from Controller.controllerEstudiante import *

class arregloEstudiante():
    def __init__(self):
        self.dataEstudiante = []
        self.cargar()
    
    def adicionarEstudiante(self, objEst):
        self.dataEstudiante.append(objEst)

    def devolverEstudiante(self, pos):
        return self.dataEstudiante[pos]

    def tamañoArregloEstudiante(self):
        return len(self.dataEstudiante)

    def cargar(self):
        archivo = open("Model/estudiante.txt", "r", encoding="UTF-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombres = columna[1]
            apellidos = columna[2]
            ciclo = columna[3]
            especialidad = columna[4].strip()
            objEst = Estudiante(codigo, nombres, apellidos, ciclo, especialidad)
            self.adicionarEstudiante(objEst)
        archivo.close()