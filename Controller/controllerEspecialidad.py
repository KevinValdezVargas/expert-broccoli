class Especialidad:

    def __init__(self, codigo, nombre, creditos, resolucion):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__resolucion = resolucion

    #METODO GET
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getCreditos(self):
        return self.__creditos
    
    def getResolucion(self):
        return self.__resolucion
    
    #METODO SET
    def setCodigo(self,codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCreditos(self, creditos):
        self.__creditos = creditos

    def setResolucion(self, resolucion):
        self.__resolucion = resolucion