from claseNodo import Nodo


class Lista:
    __tope = 0
    __indice = 0
    __comienzo: Nodo
    __actual: Nodo
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    #Los siguientes dos subprogramas son necesarios para que la lista sea iterable
    #__next__ Nos sirve para pasar iterar al siguiente elemento de la secuencia
    #__iter__ Devuelve un iterador de Python.
    def __iter__(self):
        return self
    def __next__(self):
        if self.__tope == self.__indice:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration #Lanzar una excepcion en forma manual en caso de que ya pueda pasar al siguiente elemento de la lista
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    #Agregar al final de la lista 
    def AgregarFinal(self, elemento):
        aux = self.__comienzo
        cont = 0
        if self.__comienzo == None:
                nodo = Nodo(elemento)
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
                self.__actual = nodo
                self.__tope += 1
                print ("Elemento Agregado")
        else: 
            ant = aux
            while aux != None and self.__tope>=cont:
                ant = aux
                aux = aux.getSig()
                cont += 1
            if aux == None or cont == self.__tope: #Condicion fundamental para agregar elementos al final de la lista
                nodo = Nodo(elemento)
                nodo.setSiguiente(aux)
                ant.setSiguiente(nodo)
                self.__actual = nodo
                self.__tope += 1
                print ("Elemento agregado al final")

    #Ordenar aplicando sort() y la sobrecarga correspondiente
    def Ordenar(self):
        nodo = self.__comienzo
        while nodo != None:
            p = nodo.getSig()
            while p != None:
                if nodo.getDato().apellido() > p.getDato().apellido():
                    aux = nodo.getDato
                    nodo.getDato= p.getDato
                    p.getDato= aux
                    
                p = p.getSig()
            nodo = nodo.getSig()
            
    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print ("{}".format(aux.getDato()))
            aux = aux.getSig()

    #Insertar adentro
    def insertar (self, elemento, posicion):
        aux = self.__comienzo
        cont = 0
        band = False
        if posicion <= self.__tope:
            if cont == posicion:
                if self.__comienzo == None:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(self.__comienzo)
                    self.__actual = nodo
                    self.__comienzo = nodo
                    self.__tope += 1
                    
                else:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(aux)
                    aux.setSiguiente(aux.getSig())
                    self.__actual = nodo
                    self.__tope += 1
                print("Elemento INSERTADO")
            else:
                ant = aux
                while aux != None and band == False:
                    if cont == posicion:
                        band = True
                    else:
                        aux = aux.getSig()
                        cont += 1
                if band == True:
                    nodo = Nodo(elemento)
                    nodo.setSiguiente(aux)
                    ant.setSiguiente(nodo)
                    self.__tope += 1
                print("Elemento INSERTADO")
        else:
            raise Exception ("Posicion no encontrada")
        
    #Eliminar 
    def Eliminar(self, nombre):
        aux = self.__comienzo
        band = False
        if aux.getDato().getnombre() == nombre:
            self.__comienzo = aux.getSig()
            self.__tope -= 1
            del aux
        else:
            ant = aux
            while aux != None and band == False:
                if aux.getDato().getnombre() == nombre:
                    band = True
                else:
                    ant = aux
                    aux = aux.getSig()
            if band:
                ant.setSiguiente(aux.getSig())
                self.__tope -= 1
                del aux
        print ("ELEMENTO ELIMINADO CON EXITO")