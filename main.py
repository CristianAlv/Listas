from claseNodo import Nodo
from clasePersona import Persona
from claseLista import Lista

if __name__ == '__main__':
    persona1 = Persona("Cristian", "Alvarez", 45634424)
    persona2 = Persona("Tobias", "Martin", 43432134)
    persona3 = Persona("Ana", "Maldonado", 20302484)
    persona4 = Persona("Alejandro", "Perez", 80324564)
    persona5 = Persona("Augusto", "Manrique", 44543567)
    persona6 = Persona("Joaquin", "Albornoz", 45777888)
    ListarPersonas = Lista()
    
    ListarPersonas.AgregarFinal(persona4)
    ListarPersonas.AgregarFinal(persona3)
    ListarPersonas.AgregarFinal(persona2)
    ListarPersonas.AgregarFinal(persona1)
    ListarPersonas.insertar(persona6, 1)
    ListarPersonas.mostrar()
    print ("{:|^120}".format(""))
    ListarPersonas.Ordenar()
    print ("{:|^120}".format(""))
    ListarPersonas.mostrar()
    #nombreDelete = str(input("Ingrese el nombre de la persona a eliminar: "))
    #ListarPersonas.Eliminar(nombreDelete)
    #ListarPersonas.mostrar()
