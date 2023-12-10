def mochila_recursiva(valores, pesos, capacidad, n):
    # Caso base: Si no hay elementos o la capacidad es 0, el valor y la lista de elementos son 0.
    if n == 0 or capacidad == 0:
        return 0, []

    # Si el peso del elemento n-1 es mayor que la capacidad, lo excluimos.
    if pesos[n - 1] > capacidad:
        return mochila_recursiva(valores, pesos, capacidad, n - 1)

    # Consideramos dos opciones: incluir o no incluir el elemento n-1.
    incluir_valor, incluir_elementos = mochila_recursiva(valores, pesos, capacidad - pesos[n - 1], n - 1)
    incluir_valor += valores[n - 1]
    incluir_elementos = incluir_elementos + [n - 1]  # Almacenar el índice del elemento incluido

    no_incluir_valor, no_incluir_elementos = mochila_recursiva(valores, pesos, capacidad, n - 1)

    # Seleccionamos la opción que maximiza el valor.
    if incluir_valor > no_incluir_valor:
        return incluir_valor, incluir_elementos
    else:
        return no_incluir_valor, no_incluir_elementos

# Ejemplo de uso:
valores = [220, 100, 120]
pesos = [10, 20, 30]
capacidad_mochila = 50
n = len(valores)

valor_maximo, elementos_seleccionados = mochila_recursiva(valores, pesos, capacidad_mochila, n)
print("El valor máximo que se puede obtener es:", valor_maximo)
print("Elementos seleccionados:", elementos_seleccionados)
