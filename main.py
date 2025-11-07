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
        hash_value &= 0xFFFFFFFF  

    return hex(hash_value)

# Huffman 
class Node(namedtuple('Node', ['char', 'freq', 'left', 'right'])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None
        
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    priority_queue = [Node(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None

def build_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    
    if node is None:
        return codebook
        
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def compresion(text):
    if not text:
        return "", {}
        
    root = build_huffman_tree(text)
    if root is None:
        return "", {}
        
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
    os.system("cls" if os.name == 'nt' else "clear")
    print("Ingrese la opción que requiera.")
    print("1. Ingresar texto.")
    print("2. Salir.")
    
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        input("Presione cualquier tecla para continuar.")
        continue

    if opcion == 1:
        os.system("cls" if os.name == 'nt' else "clear")
        print("Ingrese el texto a convertir.")
        textoAConvertir = input("Texto: ")
        
        if not textoAConvertir:
            print("El texto no puede estar vacío.")
        else:
            hashConvertido = hashFNV1(textoAConvertir)
            print(f"Algoritmo Hash FNV-1: {hashConvertido}")
            tamañoOriginal, tamañoComprimido = huffman_comprimido(textoAConvertir)
            print(f"Tamaño original del texto: {tamañoOriginal} bits")
            print(f"Tamaño comprimido del texto con Huffman: {tamañoComprimido} bits")
            
            if tamañoOriginal > 0:
                ratio_compresion = (tamañoComprimido / tamañoOriginal) * 100
                print(f"Ratio de compresión: {ratio_compresion:.2f}%")

        input("Presione cualquier tecla para continuar.")

    elif opcion == 2: 
        print("Rodrigo Gabriel Pérez Vásquez, 1576224.")
        detenerse = True

    else: 
        print("Ingrese una opción válida (1 o 2).")
        input("Presione cualquier tecla para continuar.")