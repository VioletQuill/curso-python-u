# Tema 4- Lección 4 Funciones anónimas lambda
# Ejecicio Ejercicio crear funciones lambda

"""
Objetivo: Crear funciones lambda para procesar una lista de números

Enunciado:Crea tres funciones lambda y asígnalas a variables con los siguientes nombres y comportamientos:

cuadrado: una función que reciba un número y devuelva su cuadrado.
es_par: una función que reciba un número y devuelva True si es par o False si es impar.
suma: una función que reciba dos números y devuelva su suma.
Luego, crea una lista llamada numeros con los valores [1, 2, 3, 4, 5] y utiliza la función map() con tu lambda 
cuadrado para crear una nueva lista llamada cuadrados que contenga el cuadrado de cada número.

Finalmente, utiliza la función filter() con tu lambda es_par para crear una lista llamada pares que contenga 
solo los números pares de la lista original.
"""

# ===================================
# ARCHIVO: ejercicio_lambda_numeros.py
# ===================================

# Crear las funciones lambda según el enunciado
cuadrado = lambda x: x ** 2
es_par = lambda x: x % 2 == 0
suma = lambda a, b: a + b

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usar map() con la lambda cuadrado
cuadrados = list(map(cuadrado, numeros))

# Usar filter() con la lambda es_par
pares = list(filter(es_par, numeros))

# Mostrar resultados
print("=== RESULTADOS DEL EJERCICIO ===")
print(f"Lista original: {numeros}")
print(f"Cuadrados (map): {cuadrados}")
print(f"Números pares (filter): {pares}")

# Pruebas adicionales de las funciones lambda
print("\n=== PRUEBAS ADICIONALES ===")
print(f"cuadrado(4) = {cuadrado(4)}")  # 16
print(f"es_par(7) = {es_par(7)}")     # False
print(f"es_par(8) = {es_par(8)}")     # True
print(f"suma(5, 3) = {suma(5, 3)}")   # 8
