class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_izquierda(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def insertar_derecha(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def remover_izquierda(self):
        if self.primero is None:
            return None
        valor = self.primero.valor
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
        return valor

    def remover_derecha(self):
        if self.primero is None:
            return None
        valor = self.ultimo.valor
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
        return valor

    def ver_izquierda(self):
        return self.primero.valor if self.primero is not None else None

    def ver_derecha(self):
        return self.ultimo.valor if self.ultimo is not None else None

    def esta_vacia(self):
        return self.primero is None

# Ejemplo de uso:
deque = Deque()
deque.insertar_izquierda(3)
deque.insertar_izquierda(2)
deque.insertar_derecha(4)
print("Deque:", [deque.ver_izquierda(), deque.ver_derecha()])

deque.remover_izquierda()
print("Deque después de remover izquierda:", [deque.ver_izquierda(), deque.ver_derecha()])
