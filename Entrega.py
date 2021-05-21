from Colonia import Colonia
from PriorityQueue import PriotityQueue
from Ciudad import Ciudad
from NodoBusqueda import NodoBusqueda
from Estado import Estado
import json
from queue import Queue


class Entrega:

    __coloniaInicial = ""
    __lugaresEntregas = []
    __costoMaximo = 0.0

    def __init__(self, coloniaInicial, lugaresEntregas, costoMaximo):
        self.__ciudad = None
        self.__coloniaInicial = coloniaInicial
        self.__lugaresEntregas = lugaresEntregas
        self.__costoMaximo = costoMaximo

    def cargarMapa(self,nombreArchivo):
        # read file
        myJsonFile = open(nombreArchivo, 'r')
        jsonData = myJsonFile.read()
        # parse
        obj = json.loads(jsonData)
        listaColonias = obj['colonias']

        #se crea la ciudad
        city = Ciudad(obj["ciudad"])        
        for i in range(len(listaColonias)):
            city.addColonia(Colonia.cargarColonia(listaColonias[i]))
            

    # función que retorna el nodo inicial de la busqueda
    def nodoInicial(self):
        coloniaInicial = self.__ciudad.getColonia(self.__coloniaInicial)
        return NodoBusqueda(Estado(coloniaInicial, self.__lugaresEntregas), None, self.__coloniaInicial, 0)

    def hacerNodoHijo(self, padre, ruta, costoRuta):
        nuevaColonia = self.__ciudad.getColonia(ruta)
        coloniasFaltantes = padre.getEstado().nuevasColoniasFaltantes(ruta)
        nuevoCosto = padre.getCostoCamino() + costoRuta
        nuevaAccion = padre.getEstado().getNombreColoniaEstado() + "->" + ruta
        return NodoBusqueda(Estado(nuevaColonia, coloniasFaltantes), padre, nuevaAccion, nuevoCosto)

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
                return False  # hacer algo failure
            nodo = frontera.pop()
            if nodo.getEstado().esEstadoMeta(self.__coloniaInicial):
                return True  # hacer algo solution
            explorados.add(nodo.getEstado())
            coloniaActual = nodo.getEstado().getColoniaEstado()
            # las rutas adyacentes son las acciones validas por lo tanto se itera através de ellas
            for ruta in coloniaActual.getRutas().keys():
                nodoHijo = self.hacerNodoHijo(
                    nodo, ruta, coloniaActual.getRutas()[ruta])
                seEncuentraFrontera = frontera.seEncuentra(nodoHijo)
                if (not self.seEncuentraExplorados(explorados, nodoHijo.getEstado())) or (seEncuentraFrontera == -1):
                    frontera.insertar(nodoHijo)
                elif seEncuentraFrontera != -1:
                    frontera.intercambiarMejorEstado(
                        nodoHijo, seEncuentraFrontera)

    def BFS(self):
        pass
