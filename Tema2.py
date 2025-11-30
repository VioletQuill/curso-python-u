# Primera Lección – Tipos de datos y operaciones 
# 1. Python tiene tipado dinámico
# No declaras el tipo. Python lo infiere:

""" Ejercicio 1: Tipos de Datos. Descomentar para probar """

"""""
age = 25
height = 1.65
is_student = True
name = "Paola"

print(age)
print(height)
print(is_student)
print(name)

"""

#Ejercicio 2: Listas. Descomentar para probar

"""

numeros = [10, 20, 30, 40, 50]

# Añadir 60 al final
numeros.append(60)

# Insertar 15 entre 10 y 20 → posición 1
numeros.insert(1, 15)

# Eliminar el número 30
numeros.remove(30)

# Calcular suma
suma = sum(numeros)

# Calcular promedio
promedio = suma / len(numeros)

# Imprimir resultados
print(numeros)
print(suma)
print(promedio)

"""
#Ejercicio 3: Crear y manipular una tupla con información de contactos.

"""_Enunciado: Crea una tupla llamada contacto que contenga la siguiente 
    información en este orden: nombre, correo electrónico y número de teléfono. 
    Utiliza los valores "Ana García", "ana@ejemplo.com" y "555-1234". 
    Luego, realiza las siguientes operaciones: Desempaqueta la tupla en tres variables 
    llamadas nombre, email y telefono. Imprime cada variable en líneas separadas. 
    Crea una nueva tupla llamada contacto_completo que contenga los elementos de la 
    tupla original más la ciudad "Madrid" al final. Recuerda que las tuplas son 
    inmutables, por lo que deberás crear una nueva tupla para añadir el elemento 
    adicional.
"""

""""
# Crear la tupla con la información del contacto
contacto = ("Ana García", "ana@ejemplo.com", "555-1234")

# Desempaquetar la tupla
nombre, email, telefono = contacto

# Imprimir cada variable en líneas separadas
print(nombre)
print(email)
print(telefono)

# Crear nueva tupla con la ciudad añadida al final
contacto_completo = contacto + ("Madrid",)

# Imprimir la nueva tupla (opcional, pero útil para ver el resultado)
print(contacto_completo)
"""

#Ejercicio 4: Diccionarios. 
# Crear un diccionario para almacenar información de contactos y acceder a sus datos

"""_Enunciado: Crea un diccionario llamado contactos que contenga la información de tres personas. Para cada persona, almacena su nombre, teléfono y correo electrónico. Luego, realiza las siguientes operaciones:

Muestra el correo electrónico de la segunda persona que añadiste al diccionario.
Añade un nuevo contacto con la información que prefieras.
Modifica el número de teléfono de la primera persona que añadiste.
Utiliza un bucle para mostrar los nombres de todos los contactos.
Puedes empezar con algo como:
    
contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    # Añade más contactos aquí
}
"""

"""# Ejercicio 4: Diccionarios.

Tu código para realizar las operaciones solicitadas
# Diccionario inicial con tres contactos
contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona2": {"nombre": "Luis", "telefono": "987654321", "email": "luis@ejemplo.com"},
    "persona3": {"nombre": "María", "telefono": "555555555", "email": "maria@ejemplo.com"}
}

# 1. Mostrar el correo electrónico de la segunda persona añadida
print(contactos["persona2"]["email"])

# 2. Añadir un nuevo contacto
contactos["persona4"] = {
    "nombre": "Carlos",
    "telefono": "111222333",
    "email": "carlos@ejemplo.com"
}

# 3. Modificar el número de teléfono de la primera persona
contactos["persona1"]["telefono"] = "000000000"

# 4. Mostrar los nombres de todos los contactos
for clave, datos in contactos.items():
    print(datos["nombre"])
"""
    
#Ejercicio 5: Estructuras de Datos: Conjuntos.

""" 
Objetivo
Crear un programa que utilice conjuntos para encontrar elementos comunes
y únicos entre dos listas.

Enunciado:
Crea un programa que trabaje con dos listas de números enteros. Debes convertir estas listas a conjuntos y realizar las siguientes operaciones:

Encuentra los elementos que aparecen en ambas listas (intersección)
Encuentra los elementos que solo aparecen en la primera lista (diferencia)
Encuentra los elementos que solo aparecen en la segunda lista (diferencia)
Encuentra todos los elementos únicos que aparecen en cualquiera de las dos listas (unión)
Utiliza las siguientes listas para tu programa:

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
Imprime el resultado de cada operación en líneas separadas.
"""

"""
# Listas proporcionadas
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

# Convertir listas a conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Operaciones con conjuntos
elementos_comunes = conjunto1 & conjunto2  # Intersección
solo_en_lista1 = conjunto1 - conjunto2     # Diferencia (lista1 - lista2)
solo_en_lista2 = conjunto2 - conjunto1     # Diferencia (lista2 - lista1)
todos_elementos = conjunto1 | conjunto2    # Unión

# Imprimir resultados
print(elementos_comunes)
print(solo_en_lista1)
print(solo_en_lista2)
print(todos_elementos)
"""
#Ejercicio 6: Collections

"""
Objetivo: rear una función que utilice Counter para analizar frecuencias 
de caracteres en un texto

Enunciado: Implementa una función llamada analizar_texto que reciba como parámetro 
una cadena de texto y devuelva un diccionario con las siguientes estadísticas:

caracteres_mas_comunes: Una lista con los 3 caracteres más comunes y su frecuencia, 
excluyendo espacios en blanco. El formato debe ser una lista de tuplas 
(caracter, frecuencia).

total_caracteres: El número total de caracteres en el texto, incluyendo espacios.

total_sin_espacios: El número total de caracteres excluyendo espacios en blanco.

Utiliza la clase Counter del módulo collections para realizar el análisis 
de frecuencias.

Ejemplo de uso:

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)
# Debería imprimir algo como:
# {'caracteres_mas_comunes': [('e', 4), ('o', 3), ('l', 2)], 
# 'total_caracteres': 32, 'total_sin_espacios': 27}
"""

from collections import Counter

def analizar_texto(texto):
    total_caracteres = len(texto)
    texto_sin_espacios = texto.replace(" ", "")
    total_sin_espacios = len(texto_sin_espacios)
    
    contador = Counter(texto_sin_espacios)
    caracteres_mas_comunes = contador.most_common(3)
    
    return {
        'caracteres_mas_comunes': caracteres_mas_comunes,
        'total_caracteres': total_caracteres,
        'total_sin_espacios': total_sin_espacios
    }

# Ejemplo de uso
resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)