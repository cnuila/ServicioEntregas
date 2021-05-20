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

    def getNombreColoniaEstado(self):
        return self.__coloniaEstado.getNombre()
    
    def nuevasColoniasFaltantes(self, coloniaRemover):
        nuevaLista = []
        for colonia in self.__listaColoniasFaltantes:
            if coloniaRemover != colonia:
                nuevaLista.append(colonia)
        return nuevaLista
