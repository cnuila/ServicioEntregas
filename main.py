from Entrega import Entrega
import sys

def menu():
    print("-----------------------------------")
    print("1) BFS")
    print("2) Busqueda de Costo Uniforme")
    print("3) A*")
    print("4) Salir")
    opcion = int(input("Ingrese la opcion a realizar: "))
    print("-----------------------------------")
    return opcion

def leerArchivoProblema(nombreArchivo):
    with open(nombreArchivo, "r") as archivo:
        datos = archivo.readlines()
    return datos

def crearEntrega():
    datosArchivo = leerArchivoProblema(sys.argv[2])
    lugaresEntregas = []
    for indice, dato in enumerate(datosArchivo):
        if indice == 0:
            ubicacionInicial = dato.strip()
        elif indice == 1:
            costoMaximo = float(dato.strip())
        else:
            lugaresEntregas.append(dato.strip())
    return Entrega(ubicacionInicial, lugaresEntregas, costoMaximo)

def main():
    print("Mini proyecto Sistemas Inteligentes")
    print("-----------------------------------")
    #cargar Archivos
    servicioEntregas = crearEntrega()
    servicioEntregas.cargarMapa(sys.argv[1])
    print("Se cargo el mapa correctamente.")
    
    opcion = 0
    while opcion != 4:        
        opcion = menu()
        if opcion == 1:
            print("Ya hable")

if __name__ == "__main__":
    main()