from Colonia import Colonia
from PriorityQueue import PriotityQueue
from Ciudad import Ciudad
from NodoBusqueda import NodoBusqueda
from Estado import Estado
import json
class Entrega:

    def __init__(self):
        self.__ciudad = None
        self.__coloniaInicial = ""
        self.__lugaresEntregas = []
        self.__costoMaximo = 0

    def cargarMapa(nombreArchivo):
        # read file
        myJsonFile = open(nombreArchivo, 'r')
        JsonData = myJsonFile.read()
        # parse
        obj = json.loads(JsonData)
        listaColonias = obj['colonias']

        #se crea la ciudad
        city = Ciudad(obj["ciudad"])
        
        for i in range(len(listaColonias)):
            city.getColonias().append(Colonia.cargarColonias(listaColonias[i]))
            

    #función que retorna el nodo inicial de la busqueda
    def nodoInicial(self):
        coloniaInicial = self.__ciudad.getColonia(self.__coloniaInicial)
        return NodoBusqueda(Estado(coloniaInicial, self.__lugaresEntregas),None,self.__coloniaInicial,0)

    def hacerNodoHijo(self, padre, ruta, costoRuta):
        nuevaColonia = self.__ciudad.getColonia(ruta)
        coloniasFaltantes = padre.getEstado().nuevasColoniasFaltantes(ruta)
        nuevoCosto = padre.getCostoCamino() + costoRuta
        nuevaAccion = padre.getEstado().getNombreColoniaEstado() + "->" + ruta
        return NodoBusqueda(Estado(nuevaColonia,coloniasFaltantes),padre,nuevaAccion,nuevoCosto)
    
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
            #las rutas adyacentes son las acciones validas por lo tanto se itera através de ellas
            for ruta in coloniaActual.getRutas().keys():                
                nodoHijo = self.hacerNodoHijo(nodo,ruta,coloniaActual.getRutas()[ruta])
                seEncuentraFrontera = frontera.seEncuentra(nodoHijo)
                if (not self.seEncuentraExplorados(explorados, nodoHijo.getEstado())) or (seEncuentraFrontera == -1):
                    frontera.insertar(nodoHijo)
                elif seEncuentraFrontera != -1:                     
                    frontera.intercambiarMejorEstado(nodoHijo,seEncuentraFrontera)
    
    def BFS(self):
        pass

