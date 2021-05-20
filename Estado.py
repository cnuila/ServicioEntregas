class Estado():
    
    __coloniaEstado = None
    __listaColoniasFaltantes = []
    
    def __init__(self, coloniaEstado, listaColoniasFaltantes):
        self.__coloniaEstado = coloniaEstado
        self.__listaColoniasFaltantes = listaColoniasFaltantes
    
    def esEstadoMeta(self, destino):
        if (self.__coloniaEstado == destino) and (len(self.__listaColoniasFaltantes) == 0):
            return True
        return False

    def getColoniaEstado(self):
        return self.__coloniaEstado
