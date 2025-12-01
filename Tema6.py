#Tema 6- Gestión de Excepciones

"""
Objetivo
Crear un programa que capture y maneje excepciones al solicitar un número entero por consola.

Enunciado: Crea un programa que solicite al usuario introducir un número entero por consola. 
El programa debe manejar posibles errores utilizando un bloque try-except:

Si el usuario introduce algo que no es un número entero, debe capturar la excepción ValueError y mostrar el 
mensaje: "Error: Debes introducir un número entero."

Si el usuario interrumpe la ejecución (por ejemplo, con Ctrl+C), debe capturar la excepción KeyboardInterrupt 
y mostrar el mensaje: "Se ha interrumpido la ejecución del programa."

Si la operación se completa correctamente, debe mostrar: "Has introducido el número: [número]".

Para empezar, utiliza la función input() para solicitar la entrada y la función int() para convertirla a entero 
dentro del bloque try.
"""


#Solución ejercicio:

try:
    # Solicitar número entero por consola
    entrada = input("Introduce un número entero: ")
    numero = int(entrada)
    print(f"Has introducido el número: {numero}")
    
except ValueError:
    # Capturar error cuando no se introduce un número entero válido
    print("Error: Debes introducir un número entero.")
    
except KeyboardInterrupt:
    # Capturar interrupción del usuario (Ctrl+C)
    print("Se ha interrumpido la ejecución del programa.")


#Lección 2: Filtrar y transformar datos

"""
Objetivo: Filtrar números pares y duplicarlos usando filter() y map()

Enunciado: Dada una lista de números enteros, crea una función llamada procesar_numeros que realice las 
siguientes operaciones:

Filtra solo los números pares de la lista usando la función filter()
Aplica una transformación a cada número par para duplicar su valor usando la función map()
Devuelve una lista con los resultados
Por ejemplo, si la entrada es [1, 2, 3, 4, 5, 6], la salida debe ser [4, 8, 12] (los números pares 2, 4 y 6 
filtrados y luego duplicados).
"""

#Solución ejercicio:


def procesar_numeros(numeros):
    """
    Filtra números pares y los duplica usando filter() y map()
    
    Args:
        numeros: Lista de números enteros
        
    Returns:
        Lista con los números pares duplicados
    """
    # Paso 1: Filtrar solo los números pares usando filter()
    numeros_pares = filter(lambda x: x % 2 == 0, numeros)
    
    # Paso 2: Duplicar cada número par usando map()
    numeros_duplicados = map(lambda x: x * 2, numeros_pares)
    
    # Paso 3: Convertir a lista y devolver el resultado
    return list(numeros_duplicados)

# Ejemplo de uso
if __name__ == "__main__":
    # Prueba con el ejemplo dado
    entrada = [1, 2, 3, 4, 5, 6]
    resultado = procesar_numeros(entrada)
    print(f"Entrada: {entrada}")
    print(f"Salida: {resultado}")  # [4, 8, 12]
    
    # Más pruebas
    print(f"\nOtras pruebas:")
    print(f"procesar_numeros([10, 15, 20, 25]): {procesar_numeros([10, 15, 20, 25])}")  # [20, 40]
    print(f"procesar_numeros([1, 3, 5]): {procesar_numeros([1, 3, 5])}")  # []
    print(f"procesar_numeros([2, 4, 6, 8]): {procesar_numeros([2, 4, 6, 8])}")  # [4, 8, 12, 16]


# Lección 3: Comprehensions

#Ejercicio
"""
Obejtivo: Objetivo
Crear una lista de palabras en mayúsculas que tengan más de 4 letras
Enunciado: Dada la siguiente lista de palabras: ["python", "programación", "lista", "comprehension", "for", 
"if", "else", "diccionario"]

Utiliza una list comprehension para crear una nueva lista que contenga solo las palabras que tienen más de 4 
letras, y además, convierte estas palabras a mayúsculas.

Por ejemplo, si la lista original fuera ["hola", "mundo", "python"], el resultado sería ["MUNDO", "PYTHON"] 
porque "hola" tiene 4 letras exactamente y no cumple la condición de tener más de 4 letras.
"""


#Solución ejercicio:

# Lista original de palabras
palabras = ["python", "programación", "lista", "comprehension", "for", "if", "else", "diccionario"]

# List comprehension para filtrar palabras con más de 4 letras y convertirlas a mayúsculas
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]

# Mostrar el resultado
print("Lista original:", palabras)
print("Palabras con más de 4 letras en mayúsculas:", palabras_filtradas)


#Lección 4 Iteración múltiple

#Ejercicio:
"""
Objetivo
Crear una matriz de multiplicación con bucles anidados

Enunciado: Crea una matriz de multiplicación de 5x5 utilizando bucles anidados. La matriz debe contener el 
resultado de multiplicar el número de fila por el número de columna. Por ejemplo, en la posición [2][3] debe 
estar el valor 6 (2×3). Después de crear la matriz, muestra su contenido en la consola con un formato de tabla, 
donde cada fila aparezca en una línea diferente y los números estén separados por espacios.
"""

# Crear una matriz de multiplicación 5x5
matriz = []

# Usar bucles anidados para llenar la matriz
for i in range(1, 6):  # Filas del 1 al 5
    fila = []
    for j in range(1, 6):  # Columnas del 1 al 5
        # Multiplicar el número de fila por el número de columna
        resultado = i * j
        fila.append(resultado)
    matriz.append(fila)

# Mostrar la matriz en formato de tabla
print("Matriz de multiplicación 5x5:")
for fila in matriz:
    # Convertir cada número a string y formatear con espacios
    fila_formateada = [str(num).rjust(3) for num in fila]
    print(" ".join(fila_formateada))
    
    # Lección 5: Generadores
    
    #Ejercicio
    
"""
Objetivo
Crear un generador que produzca los primeros n números de la secuencia de Fibonacci

Enunciado: Implementa un generador llamado fibonacci_generator que produzca los primeros n números de 
la secuencia de Fibonacci. La secuencia de Fibonacci comienza con 0 y 1, y cada número siguiente es la suma de 
los dos anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). La función debe aceptar un parámetro n que indique cuántos 
números de la secuencia debe generar. Si n es menor o igual a 0, el generador no debe producir ningún valor.

Por ejemplo, si llamamos a fibonacci_generator(6), debería generar los valores: 0, 1, 1, 2, 3, 5.
"""

# Solución

def fibonacci_generator(n):
    """
    Generador que produce los primeros n números de la secuencia de Fibonacci.
    
    Args:
        n: Cantidad de números de Fibonacci a generar
    
    Yields:
        Los primeros n números de la secuencia de Fibonacci
    """
    # Si n es menor o igual a 0, no generamos ningún valor
    if n <= 0:
        return
    
    # Casos base de la secuencia de Fibonacci
    a, b = 0, 1
    
    # Generamos los primeros n números
    for _ in range(n):
        yield a
        a, b = b, a + b

# Pruebas del generador
if __name__ == "__main__":
    print("Primeros 6 números de Fibonacci:")
    for num in fibonacci_generator(6):
        print(num, end=" ")
    # Salida esperada: 0 1 1 2 3 5
    
    print("\n\nPrimeros 10 números de Fibonacci:")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    # Salida esperada: 0 1 1 2 3 5 8 13 21 34
    
    print("\n\nPrueba con n=0:")
    resultado = list(fibonacci_generator(0))
    print(f"Resultado: {resultado}")  # Debe ser una lista vacía
    
    print("\nPrueba con n=1:")
    resultado = list(fibonacci_generator(1))
    print(f"Resultado: {resultado}")  # Debe ser [0]
    
    print("\nPrueba con n=2:")
    resultado = list(fibonacci_generator(2))
    print(f"Resultado: {resultado}")  # Debe ser [0, 1]