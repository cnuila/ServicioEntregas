class Estado():
    
    __coloniaActual = None
    __listaColoniasFaltantes = []
    
    def __init__(self, coloniaActual, listaColoniasFaltantes):
        self.__coloniaActual = coloniaActual
        self.__listaColoniasFaltantes = listaColoniasFaltantes
    
    def esEstadoMeta(self, destino):
        if (self.__coloniaActual == destino) and (len(self.__listaColoniasFaltantes) == 0):
            return True
        return False
    

