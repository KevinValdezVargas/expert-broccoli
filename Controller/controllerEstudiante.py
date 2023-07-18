class Estudiante:

    def __init__(self, codigo, nombres, apellidos, ciclo, especialidad):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__ciclo = ciclo
        self.__especialidad = especialidad

    # MÉTODOS GET AND SET

    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self,codigo):
        self.__codigo = codigo
    
    
    def getNombres(self):
        return self.__nombres
    
    def setNombres(self,nombres):
        self.__nombres = nombres
    

    def getApellidos(self):
        return self.__apellidos
    
    def setApellidos(self,apellidos):
        self.__apellidos = apellidos
    

    def getCiclo(self):
        return self.__ciclo
    
    def setCiclo(self,ciclo):
        self.__ciclo = ciclo
    

    def getEspecialidad(self):
        return self.__especialidad
    
    def setEspecialidad(self,especialidad):
        self.__especialidad = especialidad