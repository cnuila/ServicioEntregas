class Ciudad:
    
    __nombre = ""
    __colonias = []
    
    def __init__(self, nombre):
        self.__nombre = nombre

    def getColonia(self, nombreColonia):
        for colonia in self.__colonias:
            if colonia.getNombre() == nombreColonia:
                return colonia
    
    def getColonias(self):
        return self.__colonias