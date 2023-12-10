def ordenar_cartas(cartas):
    # Inicializar la primera mano con la pila de cartas barajadas
    primera_mano = [cartas.pop(0)]

    while cartas:
        # Tomar la siguiente carta visible
        carta_visible = cartas.pop(0)

        # Elegir entre colocar la carta al frente o al final de la pila en la primera mano
        if carta_visible < primera_mano[0]:
            primera_mano.insert(0, carta_visible)  # Colocar al frente
        else:
            primera_mano.append(carta_visible)  # Colocar al final

    return primera_mano

# Ejemplo de uso:
cartas_espadas = [2, 4, 7, 10, 5, 8, 3, 6, 1, 9, 13, 11, 12]
print("Cartas desordenadas:", cartas_espadas)

mano_ordenada = ordenar_cartas(cartas_espadas)

print("Cartas ordenadas:", mano_ordenada)
