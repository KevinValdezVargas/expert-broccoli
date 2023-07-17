class Especialidad:

    def __init__(self, codigo, nombre, creditos, resolucion):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__resolucion = resolucion

    #METODO GET
    def getcodigo(self):
        return self.__codigo
    
    def getnombre(self):
        return self.__nombre
    
    def getcreditos(self):
        return self.__creditos
    
    def getresolucion(self):
        return self.__resolucion
    
    #METODO SET
    def setcodigo(self,codigo):
        self.__codigo = codigo

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setcreditos(self, creditos):
        self.__creditos = creditos

    def setresolucion(self, resolucion):
        self.__resolucion = resolucion