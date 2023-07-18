from Controller.controllerEspecialidad import *

class arregloEspecialidad:

    def __init__(self):
        self.dataEspecialidad = []
        self.cargar()

    def adicionaEspecialidad(self, objEspe):
        self.dataEspecialidad.append(objEspe)

    def devolverEspecialidad(self, pos):
        return self.dataEspecialidad[pos]
    
    def tamañoArregloEspecialidad(self):
        return len(self.dataEspecialidad)
        
    def cargar(self):
        archivo = open("Model/especialidad.txt", "r", encoding="UTF-8")

        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombre = columna[1]
            creditos = columna[2]
            resolucion = columna[3].strip()
            objEspe = Especialidad(codigo, nombre, creditos, resolucion)
            self.adicionaEspecialidad(objEspe)
        archivo.close()