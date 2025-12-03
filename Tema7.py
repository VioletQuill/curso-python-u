#Tema 7- Creación de Arrays en Numpy

"""
Objetivo
Crear diferentes tipos de arrays en NumPy utilizando métodos básicos de creación  

Enunciado:  
Crea los siguientes arrays de NumPy:

Un array unidimensional con los números del 1 al 10 utilizando array()
Una matriz de ceros de tamaño 3x3 utilizando zeros()
Un array unidimensional con 5 unos utilizando ones()
Un array con 8 valores equidistantes entre 0 y 1 (ambos incluidos) utilizando linspace()
Un array con los números pares del 2 al 20 utilizando arange()
Asegúrate de importar NumPy correctamente al inicio de tu código.
"""

#Solución

import numpy as np

# 1. Array unidimensional del 1 al 10
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# o también: np.arange(1, 11)

# 2. Matriz de ceros 3x3
matriz_ceros = np.zeros((3, 3))

# 3. Array unidimensional con 5 unos
array_unos = np.ones(5)

# 4. 8 valores equidistantes entre 0 y 1 (inclusive)
valores_equidistantes = np.linspace(0, 1, 8)

# 5. Array con números pares del 2 al 20
pares = np.arange(2, 21, 2)

# Mostrar resultados
print("1. Array del 1 al 10:")
print(array1)
print("\n2. Matriz de ceros 3x3:")
print(matriz_ceros)
print("\n3. Array con 5 unos:")
print(array_unos)
print("\n4. 8 valores equidistantes entre 0 y 1:")
print(valores_equidistantes)
print("\n5. Números pares del 2 al 20:")
print(pares)


#Lección 2: Propiedades o atributos de los Arrays en Numpy

"""Ejercicio
    Objetivo:
    Enunciado:
"""

