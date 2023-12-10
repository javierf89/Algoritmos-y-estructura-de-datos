import heapq
from collections import defaultdict

class Nodo:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.freq < otro.freq

def construir_arbol_huffman(texto):
    mapa_frecuencia = defaultdict(int)
    for char in texto:
        mapa_frecuencia[char] += 1

    monticulo = [Nodo(char, freq) for char, freq in mapa_frecuencia.items()]
    heapq.heapify(monticulo)

    while len(monticulo) > 1:
        izquierda = heapq.heappop(monticulo)
        derecha = heapq.heappop(monticulo)
        nodo_fusion = Nodo(None, izquierda.freq + derecha.freq)
        nodo_fusion.izquierda = izquierda
        nodo_fusion.derecha = derecha
        heapq.heappush(monticulo, nodo_fusion)

    return monticulo[0]

def construir_codigos_huffman(nodo, codigo_actual, mapa_codigos):
    if nodo is None:
        return
    if nodo.char:
        mapa_codigos[nodo.char] = codigo_actual
    construir_codigos_huffman(nodo.izquierda, codigo_actual + '0', mapa_codigos)
    construir_codigos_huffman(nodo.derecha, codigo_actual + '1', mapa_codigos)

def codificar_huffman(texto):
    raiz = construir_arbol_huffman(texto)
    mapa_codigos = {}
    construir_codigos_huffman(raiz, '', mapa_codigos)

    texto_codificado = ''.join(mapa_codigos[char] for char in texto)
    
    return texto_codificado, mapa_codigos

def decodificar_huffman(texto_codificado, mapa_codigos):
    mapa_codigos_invertido = {v: k for k, v in mapa_codigos.items()}
    texto_decodificado = ''
    codigo_actual = ''
    
    for bit in texto_codificado:
        codigo_actual += bit
        if codigo_actual in mapa_codigos_invertido:
            texto_decodificado += mapa_codigos_invertido[codigo_actual]
            codigo_actual = ''
    
    return texto_decodificado

if __name__ == '__main__':
    texto = input("Ingresa un mensaje de texto: ")

    texto_codificado, mapa_codigos = codificar_huffman(texto)
    texto_decodificado = decodificar_huffman(texto_codificado, mapa_codigos)

    print("Longitud del mensaje original (caracteres):", len(texto))
    print("Longitud del mensaje codificado (bits):", len(texto_codificado))
    print("Codigos Huffman:")
    for char, codigo in mapa_codigos.items():
        print(f"'{char}': {codigo}")

    print("Mensaje decodificado:", texto_decodificado)
