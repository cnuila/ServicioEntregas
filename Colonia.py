class Colonia:

    __nombre = ""
    __rutas = {}

    def __init__(self, nombre, rutas):
        self.__nombre = nombre
        self.__rutas = rutas

    def getNombre(self):
        return self.__nombre
    
    def getRutas(self):
        return self.__rutas

    @staticmethod
    def cargarColonias(file):
        pass