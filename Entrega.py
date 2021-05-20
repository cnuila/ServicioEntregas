from ServicioEntregas.PriorityQueue import PriotityQueue
from ServicioEntregas.Ciudad import Ciudad
from ServicioEntregas.NodoBusqueda import NodoBusqueda
from ServicioEntregas.Estado import Estado

class Entrega:

    def __init__(self):
        self.__ciudad = None
        self.__coloniaInicial = ""
        self.__lugaresEntregas = []
        self.__costoMaximo = 0

    def cargarMapa(nombreArchivo):
        pass

    def nodoInicial(self):
        coloniaInicial = self.__ciudad.coloniaInicial(self.__coloniaInicial)
        return NodoBusqueda(Estado(coloniaInicial, self.__lugaresEntregas),None,self.__coloniaInicial,0)

    def uniformCostSearch(self):
        nodo = self.nodoInicial()
        frontera = PriotityQueue()
        frontera.insertar(nodo)
        explorados = set()
        while True:
            if frontera.estaVacia():
                return False #hacer algo failure
            if nodo.getEstado.esEstadoMeta(self.__coloniaInicial):
                return True #hacer algo solution
            explorados.add(nodo.getEstado)
            colonia = nodo.getEstado.getColoniaEstado()
            for ruta in colonia.getRutas().keys():
                #child node buscar colonia en la ciudad
                pass
