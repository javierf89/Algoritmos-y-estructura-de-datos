import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def linear_probe(self, key, index):
        return (index + 1) % self.size

    def quadratic_probe(self, key, index):
        return (index + (index ** 2)) % self.size

    def double_hash(self, key, index):
        hash2 = 7 - (key % 7)  # Una elección común para la segunda función hash
        return (index + hash2) % self.size

    def insert(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            index = self.linear_probe(key, index)  # Cambia esto para cuadrática o doble hash

        self.table[index] = key

    def find_displaced_keys(self):
        displaced_keys = []
        for i in range(self.size):
            if self.table[i] is not None and self.hash(self.table[i]) != i:
                displaced_keys.append(self.table[i])
        return displaced_keys

def test_hash_table(factor_carga, esquema_sondas):
    size = int(1000 / factor_carga)
    hash_table = HashTable(size)
    keys = [random.randint(0, 999) for _ in range(200)]

    for key in keys:
        hash_table.insert(key)

    claves_desplazadas = hash_table.find_displaced_keys()
    cantidad_desplazadas = len(claves_desplazadas)

    print(f"Factor de Carga: {factor_carga}, Esquema de Sondas: {esquema_sondas}, Cantidad de Claves Desplazadas: {cantidad_desplazadas}")

# Prueba diferentes condiciones
factores_carga = [0.5, 0.7, 0.9]
esquemas_sondas = ['Lineal', 'Cuadrática', 'Doble']

for factor_carga in factores_carga:
    for esquema_sondas in esquemas_sondas:
        test_hash_table(factor_carga, esquema_sondas)
