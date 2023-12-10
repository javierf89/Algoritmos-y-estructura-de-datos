def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        # Bandera para verificar si hubo algún intercambio en este pase
        intercambiado = False

        # Recorre el array de izquierda a derecha
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambiado = True

        # Si no hubo intercambios en el pase de izquierda a derecha, rompe el bucle
        if not intercambiado:
            break

        # Recorre el array de derecha a izquierda
        for k in range(n-i-1, 0, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]

    return arr

# Ejemplo de uso:
arr_desordenado = [64, 25, 12, 22, 11]
print("Array desordenado:", arr_desordenado)

arr_ordenado = bubbleSort(arr_desordenado)
print("Array ordenado:", arr_ordenado)
