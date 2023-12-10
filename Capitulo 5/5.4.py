class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class CircularList:
    def __init__(self):
        self.__last = None

    def esta_vacia(self):
        return self.__last is None

    def insertar_primero(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if self.esta_vacia():
            self.__last = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__last.siguiente
            self.__last.siguiente = nuevo_nodo

    def insertar_ultimo(self, valor):
        self.insertar_primero(valor)
        self.__last = self.__last.siguiente

    def eliminar_primero(self):
        if not self.esta_vacia():
            if self.__last.siguiente == self.__last:
                self.__last = None
            else:
                self.__last.siguiente = self.__last.siguiente.siguiente

    def buscar(self, clave):
        actual = self.__last
        if not self.esta_vacia():
            actual = actual.siguiente
            while actual != self.__last.siguiente:
                if actual.valor == clave:
                    return True
                actual = actual.siguiente
        return False

    def __str__(self):
        resultado = []
        actual = self.__last
        if not self.esta_vacia():
            actual = actual.siguiente
            while actual != self.__last.siguiente:
                resultado.append(actual.valor)
                actual = actual.siguiente
        return " -> ".join(map(str, resultado))

    def avanzar(self):
        if not self.esta_vacia():
            self.__last = self.__last.siguiente

    def buscar_avanzar(self, clave):
        actual = self.__last
        if not self.esta_vacia():
            actual = actual.siguiente
            while actual != self.__last.siguiente:
                if actual.valor == clave:
                    self.__last = actual
                    return True
                actual = actual.siguiente
        return False

# Ejemplo de uso:
lista_circular = CircularList()
print("¿La lista está vacía?", lista_circular.esta_vacia())

lista_circular.insertar_primero(3)
lista_circular.insertar_primero(2)
lista_circular.insertar_ultimo(4)

print("Lista circular:", lista_circular)
print("¿La lista está vacía?", lista_circular.esta_vacia())

lista_circular.eliminar_primero()
print("Lista circular después de eliminar el primero:", lista_circular)

print("¿La clave '2' está en la lista?", lista_circular.buscar(2))
print("¿La clave '5' está en la lista?", lista_circular.buscar(5))

lista_circular.avanzar()
print("Lista circular después de avanzar:", lista_circular)

print("¿La clave '3' está en la lista después de avanzar?", lista_circular.buscar_avanzar(3))
