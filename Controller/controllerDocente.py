class Docente:

    def __init__(self, codigo, nombres, apellidos, dni, gradoAcademico):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni
        self.__gradoAcademico = gradoAcademico

    def getNombres(self):
        return self.__nombres

    def setNombres(self, nombres):
        self.__nombres = nombres

    def getApellidos(self):
        return self.__apellidos

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getGradoAcademico(self):
        return self.__gradoAcademico

    def setGradoAcademico(self, gradoAcademico):
        self.__gradoAcademico = gradoAcademico

