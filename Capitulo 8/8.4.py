class NodoArbolBinario:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return NodoArbolBinario(clave, valor)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor
        return nodo

    def imprimir_arbol(self):
        self._imprimir_arbol(self.raiz)

    def _imprimir_arbol(self, nodo):
        if nodo:
            self._imprimir_arbol(nodo.izquierda)
            print(f"{nodo.clave}: {nodo.valor}")
            self._imprimir_arbol(nodo.derecha)

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self._altura(nodo.izquierda)
        altura_derecha = self._altura(nodo.derecha)
        return 1 + max(altura_izquierda, altura_derecha)

    def balance_nodo(self):
        return self._balance_nodo(self.raiz)

    def _balance_nodo(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self._altura(nodo.izquierda)
        altura_derecha = self._altura(nodo.derecha)
        return altura_derecha - altura_izquierda

    def balance_nivel(self):
        return self._balance_nivel(self.raiz)

    def _balance_nivel(self, nodo):
        if nodo is None:
            return 0
        nivel_izquierda = self._altura(nodo.izquierda)
        nivel_derecha = self._altura(nodo.derecha)
        return nivel_derecha - nivel_izquierda

    def nodos_desbalanceados(self, by=1):
        return self._nodos_desbalanceados(self.raiz, by)

    def _nodos_desbalanceados(self, nodo, by):
        if nodo is None:
            return []
        balance_nodo = abs(self._balance_nodo(nodo))
        balance_nivel = abs(self._balance_nivel(nodo))
        if balance_nodo > by or balance_nivel > by:
            return [nodo.clave] + self._nodos_desbalanceados(nodo.izquierda, by) + self._nodos_desbalanceados(nodo.derecha, by)
        else:
            return []

# Ejemplo de uso:
arbol = ArbolBinarioBusqueda()

arbol.insertar(10, "A")
arbol.insertar(5, "B")
arbol.insertar(15, "C")
arbol.insertar(3, "D")
arbol.insertar(7, "E")
arbol.insertar(12, "F")
arbol.insertar(20, "G")
arbol.insertar(2, "H")
arbol.insertar(4, "I")
arbol.insertar(6, "J")
arbol.insertar(8, "K")
arbol.insertar(11, "L")
arbol.insertar(13, "M")
arbol.insertar(18, "N")
arbol.insertar(25, "O")

print("Árbol:")
arbol.imprimir_arbol()

altura_arbol = arbol.altura()
print(f"\nAltura del árbol: {altura_arbol}")

balance_nodo_raiz = arbol.balance_nodo()
print(f"Balance de nodos en la raíz: {balance_nodo_raiz}")

balance_nivel_raiz = arbol.balance_nivel()
print(f"Balance de niveles en la raíz: {balance_nivel_raiz}")

nodos_desbalanceados_1 = arbol.nodos_desbalanceados(by=1)
print(f"\nNodos desbalanceados con by=1: {nodos_desbalanceados_1}")

nodos_desbalanceados_2 = arbol.nodos_desbalanceados(by=2)
print(f"Nodos desbalanceados con by=2: {nodos_desbalanceados_2}")
