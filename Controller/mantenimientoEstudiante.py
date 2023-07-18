from Controller.controllerEstudiante import *

class mantenimientoEstudiante():
    def __init__(self):
        self.dataEstudiante = []
        self.cargar()
    
    def adicionarEstudiante(self, objEstudiante):
        self.dataEstudiante.append(objEstudiante)

    def devolverEstudiante(self, pos):
        return self.dataEstudiante[pos]

    def tamañoManteminientoEstudiante(self):
        return len(self.dataEstudiante)

    def buscarEstudiante(self, codigo):
        for i in range(self.tamañoManteminientoEstudiante()):
            if codigo == self.dataEstudiante[i].getCodigo():
                return i
            return -1
    
    def eliminarEstudiante(self, indice):
        del(self.dataEstudiante[indice])

    def modificarEstudiante(self, objEstudiante, pos):
        self.dataEstudiante[pos]=objEstudiante

    def retornarDatos(self):
        return self.dataEstudiante

#-------------------------------------------------------------------------------------------

    def cargar(self):
        archivo = open("Model/estudiante.txt", "r", encoding="UTF-8")

        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombre = columna[1]
            apellidos = columna[2]
            ciclo = columna[3]
            especialidad = columna[4].strip()
            objEstudiante = Estudiante(codigo, nombre, apellidos, ciclo, especialidad)
            self.adicionarEstudiante(objEstudiante)
        archivo.close()
    
    def grabar(self):
        archivo = open("Model/estudiante.txt", "w", encoding="UTF-8")
        for i in range (self.tamañoManteminientoEstudiante()):
            archivo.write(str(self.devolverEstudiante(i).getCodigo())) + ","
            + str(self.devolverEstudiante(i).getNombres()) + ","
            + str(self.devolverEstudiante(i).getApellidos()) + ","
            + str(self.devolverEstudiante(i).getCiclo()) + ","
            + str(self.devolverEstudiante(i).getEspecialidad()) + "\n"
        archivo.close()