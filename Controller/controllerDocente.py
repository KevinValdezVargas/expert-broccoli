class Docente:

    def __init__(self, codigo, nombres, apellidos, dni, gradoAcademico):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni
        self.__gradoAcademico = gradoAcademico

    def getnombres(self):
        return self.__nombres

    def setnombres(self, nombres):
        self.__nombres = nombres

    def getapellidos(self):
        return self.__apellidos

    def setapellidos(self, apellidos):
        self.__apellidos = apellidos

    def getcodigo(self):
        return self.__codigo

    def setcodigo(self, codigo):
        self.__codigo = codigo

    def getdni(self):
        return self.__dni

    def setdni(self, dni):
        self.__dni = dni

    def getgradoAcademico(self):
        return self.__gradoAcademico

    def setgradoAcademico(self, gradoAcademico):
        self.__gradoAcademico = gradoAcademico

