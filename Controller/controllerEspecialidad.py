class Especialidad:

    def __init__(self, codigo, nombre, creditos, resolucion):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__resolucion = resolucion

     # MÉTODOS GET AND SET

    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self,codigo):
        self.__codigo = codigo
    

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    
    def getCreditos(self):
        return self.__creditos
    
    def setCreditos(self, creditos):
        self.__creditos = creditos
    
    
    def getResolucion(self):
        return self.__resolucion
    
    def setResolucion(self, resolucion):
        self.__resolucion = resolucion
    

    

    

    