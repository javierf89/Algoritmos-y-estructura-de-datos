import random

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.displaced_counts = 0

    def hash_function(self, key):
        raise NotImplementedError("La función de hash debe ser implementada en las clases derivadas")

    def insert(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            self.displaced_counts += 1
            index = (index + 1) % self.size

        self.table[index] = key

class FoldThreeDigitsHashTable(HashTable):
    def hash_function(self, key):
        key_str = str(key)
        chunks = [key_str[i:i+3] for i in range(0, len(key_str), 3)]
        folded_value = sum(int(chunk) for chunk in chunks)
        return folded_value % self.size

class FoldTwoDigitsHashTable(HashTable):
    def hash_function(self, key):
        key_str = str(key)
        chunks = [key_str[i:i+2] for i in range(0, len(key_str), 2)]
        folded_value = sum(int(chunk) for chunk in chunks)
        return folded_value % self.size

def main():
    random_integers = random.sample(range(10000000000), 1000)

    for load_factor in [0.5, 0.7, 0.9]:
        print(f"\nFactor de carga: {load_factor}")

        table_three_digits = FoldThreeDigitsHashTable(int(1000 / load_factor))
        table_two_digits = FoldTwoDigitsHashTable(int(1000 / load_factor))

        for integer in random_integers:
            table_three_digits.insert(integer)
            table_two_digits.insert(integer)

        print("Hashing con grupos de tres dígitos:")
        print(f"Conteo de claves desplazadas: {table_three_digits.displaced_counts}")

        print("\nHashing con grupos de dos dígitos:")
        print(f"Conteo de claves desplazadas: {table_two_digits.displaced_counts}")

if __name__ == "__main__":
    main()

