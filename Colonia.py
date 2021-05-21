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
    def cargarColonia(colonia):
        rutas = {}
        nombre = colonia["nombre"]
        for colAdj in colonia["adyacentes"]:
            nombreAdj = colAdj["nombre"]
            distancia = colAdj["distancia"]
            rutas[nombreAdj] = distancia
        print("Se creo la colonia: ", nombre, "\n con su diccionario: ", rutas)
        print(rutas)
        return Colonia(nombre, rutas)
