cadena = input("INGRESE UNA CADENA DE CARACTERES: ")

def caracteres(cadena):
    cadena2= [x  for x in cadena if not x.isspace()]
    print(cadena2)
    return cadena2
caracteres(cadena)

