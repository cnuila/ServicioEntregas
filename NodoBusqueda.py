class NodoBusqueda:

    __estado = None
    __padre = None
    __accion = None
    __costoCamino = 0

    def __init__(self, estado, padre, accion, costoCamino):
        self.__estado = estado
        self.__padre = padre
        self.__accion = accion
        self.__costoCamino = costoCamino    

    def getCostoCamino(self):
        return self.__costoCamino

    def getEstado(self):
        return self.__estado
