def combinaciones(arr, k):
    if k == 0:
        return [[]]  # Caso base: no se seleccionan elementos, retorna una lista con una lista vacía
    if len(arr) == 0:
        return []  # Caso base: no hay elementos disponibles, retorna una lista vacía
    
    primero = arr[0]  # Tomamos el primer elemento
    sin_primero = arr[1:]  # Resto de la lista

    # Combinaciones que incluyen el primer elemento
    con_primero = [[primero] + c for c in combinaciones(sin_primero, k - 1)]

    # Combinaciones que no incluyen el primer elemento
    sin_primero = combinaciones(sin_primero, k)

    return con_primero + sin_primero

# Ejemplo de uso:
elementos = [1, 2, 3, 4]
k = 2  # Número de elementos en cada combinación
resultados = combinaciones(elementos, k)
print(resultados)
