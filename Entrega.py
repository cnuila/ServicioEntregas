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
        coloniaInicial = self.__ciudad.getColonia(self.__coloniaInicial)
        return NodoBusqueda(Estado(coloniaInicial, self.__lugaresEntregas),None,self.__coloniaInicial,0)

    def hacerNodoHijo(self, padre, ruta, costoRuta):
        colonia = self.__ciudad.getColonia(ruta)
        coloniasFaltantes = padre.getEstado().nuevasColoniasFaltantes(ruta)
        nuevoCosto = padre.getCostoCamino() + costoRuta
        nuevaAccion = padre.getEstado().getNombreColoniaEstado() + "->" + ruta
        return NodoBusqueda(Estado(colonia,coloniasFaltantes),padre,nuevaAccion,nuevoCosto)
    
    def seEncuentraExplorados(self, explorados, estadoBuscar):
        for estado in explorados:
            if estado == estadoBuscar:
                return True
        return False

    def uniformCostSearch(self):
        nodo = self.nodoInicial()
        frontera = PriotityQueue()
        frontera.insertar(nodo)
        explorados = set()
        while True:
            if frontera.estaVacia():
                return False #hacer algo failure
            nodo = frontera.pop()
            if nodo.getEstado().esEstadoMeta(self.__coloniaInicial):
                return True #hacer algo solution
            explorados.add(nodo.getEstado())
            coloniaActual = nodo.getEstado().getColoniaEstado()
            for ruta in coloniaActual.getRutas().keys():                
                nodoHijo = self.hacerNodoHijo(nodo,ruta,coloniaActual.getRutas()[ruta])
                if (not self.seEncuentraExplorados(explorados, nodoHijo.getEstado())) or (not frontera.seEncuentra(nodoHijo)):
                    frontera.insertar(nodoHijo)
                else: 
                    frontera.intercambiarMejorEstado(nodoHijo)
