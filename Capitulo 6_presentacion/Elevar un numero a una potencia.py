# Función recursiva para calcular x^y
def calcular_potencia(x, y):
    # Caso base: x^0 = 1
    if y == 0:
        return 1
    # Si y es par, utilizamos la propiedad (x^a)^b = x^(a*b)
    elif y % 2 == 0:
        subproblema = calcular_potencia(x, y // 2)
        return subproblema * subproblema
    # Si y es impar, utilizamos la propiedad (x^a)^b = x^(a*b)
    else:
        subproblema = calcular_potencia(x, (y - 1) // 2)
        return x * subproblema * subproblema

# Ejemplo de uso
x = 2
y = 5
resultado = calcular_potencia(x, y)
print(f"{x}^{y} = {resultado}")
