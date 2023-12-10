from SortArray import Array

# Crear un objeto Array y agregar elementos
mi_array = Array(10)
mi_array.insert(5)
mi_array.insert(2)
mi_array.insert(8)

# Calcular y mostrar la mediana
print("Array:", mi_array)
print("Mediana:", mi_array.mediana())
