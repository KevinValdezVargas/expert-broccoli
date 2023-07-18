from Controller.controllerEspecialidad import *

class mantenimientoEspecialidad:
    def __init__(self):
        self.dataEspecialidad = []
        self.cargar()

    def adicionarEspecialidad(self, objEspecialidad):
        self.dataEspecialidad.append(objEspecialidad)

    def devolverEspecialidad(self, pos):
        return self.dataEspecialidad[pos]
    
    def tamañoManteminientoEspecialidad(self):
        return len(self.dataEspecialidad)
    
    def buscarEspecialidad(self, codigo):
        for i in range(self.tamañoManteminientoEspecialidad()):
            if codigo == self.dataEspecialidad[i].getCodigo():
                return i
            return -1
        
    def eliminarEspecialidad(self, indice):
        del(self.dataEspecialidad[indice])

    def modificarEspecialidad(self, objEspecialidad, pos):
        self.dataEspecialidad[pos]=objEspecialidad

    def retornarDatos(self):
        return self.dataEspecialidad
    
#-------------------------------------------------------------------------------------------

    def cargar(self):
        archivo = open("Model/especialidad.txt", "r", encoding="UTF-8") #CARGAR LOS DATOS DEL TXT

        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombre = columna[1]
            creditos = columna[2]
            resolucion = columna[3].strip()
            objEspecialidad = Especialidad(codigo, nombre, creditos, resolucion)
            self.adicionarEspecialidad(objEspecialidad)
        archivo.close()

    def grabar(self):
        archivo = open("Model/especialidad.txt", "w", encoding="UTF-8")
        for i in range (self.tamañoManteminientoEspecialidad()):
            archivo.write(str(self.devolverEspecialidad(i).getCodigo())) + ","
            + str(self.devolverEspecialidad(i).getNombre()) + ","
            + str(self.devolverEspecialidad(i).getCreditos()) + ","
            + str(self.devolverEspecialidad(i).getResolucion()) + "\n"
        archivo.close()