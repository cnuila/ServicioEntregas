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
        self.__ciudad = Ciudad(obj["ciudad"])        
        for i in range(len(listaColonias)):
            self.__ciudad.addColonia(Colonia.cargarColonia(listaColonias[i]))            

    #función que retorna el nodo inicial de la busqueda, y recibe un boolean para saber si de
    #costo uniforme o del A*
    def nodoInicial(self,esCostoUniforme):
        coloniaInicial = self.__ciudad.getColonia(self.__coloniaInicial)
        if esCostoUniforme:
            return NodoBusqueda(Estado(coloniaInicial, self.__lugaresEntregas),None,"Inicio -> "+self.__coloniaInicial,0)
        else:
            return NodoBusqueda(Estado(coloniaInicial, self.__lugaresEntregas),None,"Inicio -> "+self.__coloniaInicial,len(self.__lugaresEntregas))            

    def hacerNodoHijo(self, padre, ruta, costoRuta, esCostoUniforme):
        nuevaColonia = self.__ciudad.getColonia(ruta)
        coloniasFaltantes = padre.getEstado().nuevasColoniasFaltantes(ruta)
        if esCostoUniforme:
            nuevoCosto = padre.getCostoCamino() + costoRuta
        else:
            nuevoCosto = padre.getCostoCamino() + costoRuta + len(coloniasFaltantes)
        nuevaAccion = padre.getEstado().getNombreColoniaEstado() + " -> " + ruta
        return NodoBusqueda(Estado(nuevaColonia,coloniasFaltantes),padre,nuevaAccion,nuevoCosto)
    
    def seEncuentraExplorados(self, explorados, estadoBuscar):
        for estado in explorados:
            if estado == estadoBuscar:
                return True
        return False                

    #función que imprime el resultado encontrado si el costo está dentro del máximo
    def solucion(self, nodo):
        recorrido = []
        costo = nodo.rutaEncontrada(self.__ciudad,recorrido)
        if costo > self.__costoMaximo:
            print("Se encontró una ruta pero mayor al costo maximo ingresado")
            print("Costo maximo: ",self.__costoMaximo)
            print("Costo encontrado: ", nodo.getCostoCamino())
        else:
            recorrido.reverse()
            print("")
            print("")
            print("¡¡Enhorabuena!!")
            print("Ruta Encontrada:")
            for ruta in recorrido:
                print(ruta)
            print("--------------------")
            print("Costo del Recorrido:")
            print(costo)
            print("")
            print("")

    def aEstrella(self):
        nodo = self.nodoInicial(False)
        frontera = PriotityQueue()
        frontera.insertar(nodo)
        explorados = set()

        while True:
            if frontera.estaVacia():
                print("")
                print("")
                print("No se encontró una ruta")
                print("")
                print("")
                return
       
            nodo = frontera.pop()
            #se busca una solución
            if nodo.getEstado().esEstadoMeta(self.__coloniaInicial):
                self.solucion(nodo)
                print("Total de nodos explorados ",len(explorados))
                print("Total de nodos descubiertos ", len(explorados) + frontera.size())
                return
            
            explorados.add(nodo.getEstado())
            coloniaActual = nodo.getEstado().getColoniaEstado()
            
            #las rutas adyacentes son las acciones validas por lo tanto se itera através de ellas
            for ruta in coloniaActual.getRutas().keys():                
                nodoHijo = self.hacerNodoHijo(nodo,ruta,coloniaActual.getRutas()[ruta],False)
                seEncuentraFrontera = frontera.seEncuentra(nodoHijo)
                if (not self.seEncuentraExplorados(explorados, nodoHijo.getEstado())) or (seEncuentraFrontera == -1):
                    frontera.insertar(nodoHijo)
                elif seEncuentraFrontera != -1:                     
                    frontera.intercambiarMejorEstado(nodoHijo,seEncuentraFrontera)

    def uniformCostSearch(self):
        nodo = self.nodoInicial(True)
        frontera = PriotityQueue()
        frontera.insertar(nodo)
        explorados = set()
        
        while True:
            if frontera.estaVacia():
                print("")
                print("")
                print("No se encontró una ruta")
                print("")
                print("")
                return

            nodo = frontera.pop()
            #se busca una solución
            if nodo.getEstado().esEstadoMeta(self.__coloniaInicial):
                self.solucion(nodo)
                print("Total de nodos explorados ",len(explorados))
                print("Total de nodos descubiertos ", len(explorados) + frontera.size())
                return

            explorados.add(nodo.getEstado())
            coloniaActual = nodo.getEstado().getColoniaEstado()

            #las rutas adyacentes son las acciones validas por lo tanto se itera através de ellas
            for ruta in coloniaActual.getRutas().keys():                
                nodoHijo = self.hacerNodoHijo(nodo,ruta,coloniaActual.getRutas()[ruta],True)
                seEncuentraFrontera = frontera.seEncuentra(nodoHijo)
                
                if (not self.seEncuentraExplorados(explorados, nodoHijo.getEstado())) or (seEncuentraFrontera == -1):
                    frontera.insertar(nodoHijo)
                elif seEncuentraFrontera != -1:
                    frontera.intercambiarMejorEstado(
                        nodoHijo, seEncuentraFrontera)

    def BFS(self):
        pass
