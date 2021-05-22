class Estado():
    
    __coloniaEstado = None
    __listaColoniasFaltantes = []
    
    def __init__(self, coloniaEstado, listaColoniasFaltantes):
        self.__coloniaEstado = coloniaEstado
        self.__listaColoniasFaltantes = listaColoniasFaltantes
    
    #función que comprueba un estado meta si la colonia actual es la misma que la recibida
    # y si la lista de colonias faltantes es menor
    def esEstadoMeta(self, destino):
        if (self.__coloniaEstado.getNombre() == destino) and (len(self.__listaColoniasFaltantes) == 0):
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
