import json


class Colonia:
    import json
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
        # read file
        myJsonFile = open(file, 'r')
        JsonData = myJsonFile.read()
        # parse
        obj = json.loads(JsonData)
        listaColonias = obj['colonias']
        cantidadColonias = len(listaColonias)
        print(cantidadColonias)
        for i in range(len(listaColonias)):
            print("Colonia: ", listaColonias[i].get("nombre"))
        listaAdyacentes = listaColonias[i]["adyacentes"]
        for j in range(len(listaAdyacentes)):
            print("Colonia Adyacente: ", listaAdyacentes[j].get("nombre"), " Distancia: ", listaAdyacentes[j].get("distancia"), "\n")
