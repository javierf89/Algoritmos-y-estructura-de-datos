class Array(object):
    def __init__(self, initialSize):    # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.nElementos = 0                # No items in array initially

    def __len__(self):                  # Special def for len() func
        return self.nElementos             # Return number of items

    def get(self, n):                   # Return the value at index n
        if 0 <= n and n < self.nElementos: # Check if n is in bounds, and
            return self.__a[n]            # only return item if in bounds

    def set(self, n, value):            # Set the value at index n
        if 0 <= n and n < self.nElementos: # Check if n is in bounds, and
            self.__a[n] = value           # only set item if in bounds

    def swap(self, j, k):               # Swap the values at 2 indices
        if (0 <= j and j < self.nElementos and # Check if indices are in
            0 <= k and k < self.nElementos): # bounds, before processing
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):             # Insert item at end
        if self.nElementos >= len(self.__a): # If array is full,
            raise Exception("Array overflow") # raise exception
        self.__a[self.nElementos] = item   # Item goes at current end
        self.nElementos += 1               # Increment number of items

    def mediana(self):
        """
        Devuelve el valor mediano en el array.
        """
        if self.nElementos == 0:
            raise Exception("El array está vacío")

        array_ordenado = sorted(self.__a[:self.nElementos])
        medio = self.nElementos // 2

        if self.nElementos % 2 == 0:
            # Si la cantidad de elementos es par, calcula el promedio de los dos valores centrales
            return (array_ordenado[medio - 1] + array_ordenado[medio]) / 2
        else:
            # Si la cantidad de elementos es impar, devuelve el valor central
            return array_ordenado[medio]

    def traverse(self, function=print): # Traverse all items
        for j in range(self.nElementos):   # and apply a function
            function(self.__a[j])

    def __str__(self):                  # Special def for str() func
        ans = "["                        # Surround with square brackets
        for i in range(self.nElementos):   # Loop through items
            if len(ans) > 1:              # Except next to left bracket,
                ans += ", "                # separate items with comma
            ans += str(self.__a[i])       # Add string form of item
        ans += "]"                       # Close with right bracket
        return ans
