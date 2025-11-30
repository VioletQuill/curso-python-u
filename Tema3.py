#Tema 3 Ejercicio Lección 1: Operadores

"""
Objetivo
Crea una calculadora básica que utilice operadores aritméticos para realizar operaciones matemáticas.

Enunciado:Crea una calculadora básica que realice las cuatro operaciones aritméticas fundamentales (suma, resta, multiplicación y división) entre dos números.

Debes solicitar al usuario que introduzca dos números y luego mostrar el resultado de las cuatro operaciones con estos números.

Para cada operación, muestra el resultado con el siguiente formato:

"La suma de X y Y es: Z"
"La resta de X y Y es: Z"
"La multiplicación de X y Y es: Z"
"La división de X y Y es: Z"
Recuerda manejar el caso especial de división por cero mostrando un mensaje apropiado.

Pista: Utiliza los operadores +, -, *, / y controla la división por cero con una estructura condicional.
"""
"""
# Solicitar los dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones y mostrar resultados con el formato exacto solicitado
print(f"La suma de {numero1} y {numero2} es: {numero1 + numero2}")
print(f"La resta de {numero1} y {numero2} es: {numero1 - numero2}")
print(f"La multiplicación de {numero1} y {numero2} es: {numero1 * numero2}")

# Manejar división por cero
if numero2 != 0:
    print(f"La división de {numero1} y {numero2} es: {numero1 / numero2}")
else:
    print(f"La división de {numero1} y {numero2} es: No se puede dividir entre cero")
    
"""

#Tema 3: Ejercicio Lección 2: Estructuras de Control Iterativo (bucles)

"""
Objetivo:
Crear un programa que determine la categoría de edad de una persona

Enunciado:
Crea un programa que solicite la edad de una persona y determine su categoría según las siguientes reglas:

Si la edad es menor que 0, mostrar "Edad no válida"
Si la edad está entre 0 y 12, mostrar "Infante"
Si la edad está entre 13 y 17, mostrar "Adolescente"
Si la edad está entre 18 y 64, mostrar "Adulto"
Si la edad es 65 o mayor, mostrar "Adulto mayor"
Utiliza una estructura if-elif-else para implementar esta lógica. 
El programa debe solicitar la edad con la función input() y convertirla a entero antes de evaluarla.
"""


# Código del programa

"""
try:
    edad = int(input("¿Cuántos años tienes? "))
    
    print(f"\nCon {edad} años eres: ", end="")
    
    if edad < 0:     print("❌ Edad no válida")
    elif edad <= 12: print("👶 Infante")
    elif edad <= 17: print("👦 Adolescente") 
    elif edad <= 64: print("👨 Adulto")
    else:            print("👵 Adulto mayor")
        
except ValueError:
    print("❌ Error: Introduce solo números")
    
"""
    
#Tema 2: Ejercicio Lección 3 Estructuras de control iterativo

#Lección 3- Ejercicio 1: 
""" Objetivo: Crear una función que sume los números pares en un rango dado 

Enunciado:
Crea una función llamada suma_pares que reciba dos parámetros: inicio y fin. La función debe calcular y devolver 
la suma de todos los números pares que se encuentran en el rango desde inicio hasta fin (ambos inclusive).

Por ejemplo:

Si llamamos suma_pares(1, 10) debe devolver 30 (2+4+6+8+10)
Si llamamos suma_pares(5, 15) debe devolver 50 (6+8+10+12+14)
Utiliza un bucle for con la función range() para iterar sobre el rango de números y suma solo aquellos 
que sean pares (pista: puedes usar el operador módulo % para verificar si un número es par).
"""

"""
#Solución Ejercicio:

def suma_pares(inicio, fin):
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

try:
    # Solicitar entrada al usuario
    inicio = int(input("Ingresa el número de inicio: "))
    fin = int(input("Ingresa el número de fin: "))
    
    # Calcular y mostrar resultado
    resultado = suma_pares(inicio, fin)
    print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
    
except ValueError:
    print("Error: Por favor ingresa números enteros válidos.")
    
"""

#Lección 3- Ejercicio 2

""" 
Objetivo
Crear un programa que utilice un bucle while para sumar números hasta alcanzar un valor objetivo

Enunciado:

Escribe un programa que sume números enteros positivos ingresados por el usuario hasta alcanzar o superar un valor 
objetivo de 100. 

El programa debe:

Inicializar una variable suma en 0 para llevar el registro de la suma acumulada
Utilizar un bucle while que se ejecute mientras la suma sea menor que 100
Dentro del bucle, solicitar al usuario que ingrese un número entero positivo
Si el usuario ingresa un valor no numérico o un número negativo, mostrar un mensaje de error y continuar solicitando un nuevo número sin añadirlo a la suma
Si el número es válido, añadirlo a la suma acumulada y mostrar el valor actual de la suma
Cuando la suma alcance o supere 100, mostrar un mensaje indicando el valor final de la suma y cuántos números válidos fueron ingresados
Puedes comenzar con este esquema:

suma = 0
contador = 0

while suma < 100:
    # Tu código aquí

# Mensaje final
"""

#Solución Ejercicio 2:

# Inicializar variables
suma = 0
contador = 0
numeros_ingresados = []

print("=== SUMADORA HASTA 100 ===")
print("Ingresa números positivos hasta que la suma alcance o supere 100")

# Bucle while que se ejecuta mientras la suma sea menor que 100
while suma < 100:
    try:
        # Mostrar progreso
        faltante = 100 - suma
        print(f"\n--- Progreso: {suma}/100 (faltan {faltante}) ---")
        
        # Solicitar número al usuario
        numero = int(input("Ingresa un número positivo: "))
        
        # Validar que el número sea positivo
        if numero < 0:
            print("❌ Error: El número debe ser positivo. Intenta nuevamente.")
            continue
            
        # Si el número es válido, procesarlo
        suma += numero
        contador += 1
        numeros_ingresados.append(numero)
        
        print(f"✅ Añadido: {numero}")
        print(f"   Suma actual: {suma}")
        
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido.")

# Mensaje final
print(f"\n{'='*40}")
print("🎉 ¡OBJETIVO ALCANZADO!")
print(f"Suma final: {suma}")
print(f"Números válidos ingresados: {contador}")
print(f"Números ingresados: {numeros_ingresados}")
print(f"Operación: {' + '.join(map(str, numeros_ingresados))} = {suma}")
