from clasePersona import Persona
class Nodo:
    __siguiente = None
    __persona = None
    def __init__ (self, lapersona):
        self.__siguiente = None
        if isinstance(lapersona, Persona):
            self.__persona = lapersona
    def getDato(self):
        return self.__persona
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSig(self):
        return self.__siguiente
    