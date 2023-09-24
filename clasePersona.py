class Persona:
    __dni: int
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    def getnombre(self):
        return self.__nombre
    def apellido(self):
        return self.__apellido
    def getdni(self):
        return self.__dni
    

    def __lt__(self, other):
        return self.__dni < other.getdni()
    
    def __str__(self):
        return f"Dni: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}"
    
