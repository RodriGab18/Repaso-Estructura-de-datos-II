import os
import heapq
from collections import defaultdict, namedtuple

# Algoritmo Hash FNV - 1
def hashFNV1(text):
    FNV_prime = 0x01000193  
    FNV_offset_basis = 0x811c9dc5  

    data = text.encode('utf-8')
    hash_value = FNV_offset_basis

    for byte in data:
        hash_value ^= byte  
        hash_value *= FNV_prime  

    return hex(hash_value)

# Huffman 
class Node(namedtuple('Node', ['char', 'freq'])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_codes(node, prefix='', codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def compresion(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    compressed_text = ''.join(codes[char] for char in text)
    return compressed_text, codes

def calcular_tamaño(original_text, compressed_text):
    original_size = len(original_text) * 8  
    compressed_size = len(compressed_text)  
    return original_size, compressed_size

def huffman_comprimido(text):
    compressed_text, _ = compresion(text)
    original_size, compressed_size = calcular_tamaño(text, compressed_text)
    return original_size, compressed_size

# Interfaz principal
detenerse = False

while not detenerse:
    os.system("cls")
    print("Ingrese la opción que requiera.")
    print("1. Ingresar texto.")
    print("2. Salir.")
    opcion = int(input("Opción: "))

    if opcion == 1:
        os.system("cls")
        print("Ingrese el texto a convertir.")
        textoAConvertir = input("Texto: ")
        hashConvertido = hashFNV1(textoAConvertir)
        print(f"Algoritmo Hash FNV-1: {hashConvertido}")
        tamañoOriginal, tamañoComprimido = huffman_comprimido(textoAConvertir)
        print(f"Tamaño original del texto: {tamañoOriginal} bits")
        print(f"Tamaño comprimido del texto con Huffman: {tamañoComprimido} bits")

        input("Presione cualquier tecla para continuar.")

    elif opcion == 2: 
        print("Rodrigo Gabriel Pérez Vásquez, 1576224.")
        detenerse = True

    else: 
        print("Ingrese una opción válida.")