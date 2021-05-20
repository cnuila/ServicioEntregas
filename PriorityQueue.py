class PriotityQueue:    

    def __init__(self):
        self.queue = []

    def estaVacia(self):
        return len(self.queue) == 0

    def insertar(self, nodo):
        costoNodo = nodo.getCostoCamino()
        indice = -1
        for elemento in self.queue:
            if elemento.getCostoCamino() <= costoNodo:
                indice+=1
            else:
                break
        if indice == -1:
            self.queue.insert(0,nodo)
        else:
            self.queue.insert(indice,nodo)
    
    def pop(self):
        del self.queue[0]

    def seEncuentra(self, nodoBuscar):
        for nodo in self.queue:
            if nodoBuscar == nodo:
                return True
        return False

    def intercambiarMejorEstado(self, nodoBuscar):
        indice = 0
        for nodo in self.queue:
            if nodoBuscar.getEstado() == nodo.getEstado():
                if nodoBuscar.getCostoCamino() < nodo.getCostoCamino():
                    self.queue[indice] = nodoBuscar
            indice+=1
