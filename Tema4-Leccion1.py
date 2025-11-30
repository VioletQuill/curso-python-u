# Tema 4- Lección 1: Funciones matemáticas y números aleatorios

#Lección 1- Ejercicio 1: Ejercicio generar datos aleatorios

"""    
Objetivo
Crear una función que genere datos aleatorios para un conjunto de usuarios

Enunciado: 

Crea una función llamada generar_usuarios que genere datos aleatorios para un conjunto de usuarios. 
La función debe recibir como parámetro el número de usuarios a generar y devolver una lista de diccionarios, 
donde cada diccionario representa un usuario con los siguientes campos:

id: un número entero único para cada usuario (comenzando desde 1)
nombre: un nombre aleatorio elegido de una lista predefinida
edad: un número entero aleatorio entre 18 y 65
puntuacion: un número flotante aleatorio entre 0.0 y 10.0 (con un decimal)
Para implementar esta función, deberás:

Crear una lista de posibles nombres (al menos 5 nombres diferentes)
Utilizar random.randint() para generar las edades
Utilizar random.uniform() para generar las puntuaciones
Redondear las puntuaciones a 1 decimal
Ejemplo de uso:

usuarios = generar_usuarios(3)
print(usuarios)
Ejemplo de salida:

[
  {'id': 1, 'nombre': 'Ana', 'edad': 25, 'puntuacion': 8.7},
  {'id': 2, 'nombre': 'Carlos', 'edad': 42, 'puntuacion': 6.3},
  {'id': 3, 'nombre': 'Elena', 'edad': 31, 'puntuacion': 9.5}
  
  Estructura: 
  
  // ===================================
// ARCHIVO 1: main.py
// ===================================

// Escribe aquí el código de tu archivo principal


// ===================================
// ARCHIVO 2: utils.py
// ===================================

// Escribe aquí el código de tus utilidades


// ===================================
// Instrucciones:
// - Separa cada archivo con comentarios como se muestra arriba
// - Indica claramente el nombre de cada archivo
// - Borra este ejemplo y escribe tu solución
// ===================================
"""

#Solución: Ejercicio 1

# ===================================
# ARCHIVO 1: main.py
# ===================================

from utils import generar_usuarios, mostrar_usuarios, analizar_usuarios

def main():
    """Función principal del programa"""
    print("=== GENERADOR DE USUARIOS ALEATORIOS ===\n")
    
    try:
        # Solicitar número de usuarios al usuario
        num_usuarios = int(input("¿Cuántos usuarios deseas generar? "))
        
        if num_usuarios <= 0:
            print("Por favor, ingresa un número mayor que 0.")
            return
        
        # Generar usuarios
        usuarios = generar_usuarios(num_usuarios)
        
        # Mostrar resultados
        print(f"\n--- {num_usuarios} USUARIOS GENERADOS ---")
        mostrar_usuarios(usuarios)
        
        # Mostrar análisis estadístico
        print(f"\n--- ANÁLISIS ESTADÍSTICO ---")
        analizar_usuarios(usuarios)
        
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()


# ===================================
# ARCHIVO 2: utils.py
# ===================================

import random
from typing import List, Dict

# Lista de nombres predefinidos
NOMBRES = [
    "Ana", "Carlos", "Elena", "David", "Laura", 
    "Miguel", "Sofía", "Pablo", "Isabel", "Javier",
    "María", "Luis", "Carmen", "José", "Rosa",
    "Francisco", "Teresa", "Antonio", "Dolores", "Manuel"
]

def generar_usuarios(num_usuarios: int) -> List[Dict]:
    """
    Genera datos aleatorios para un conjunto de usuarios.
    
    Args:
        num_usuarios (int): Número de usuarios a generar
        
    Returns:
        List[Dict]: Lista de diccionarios con datos de usuarios
    """
    if num_usuarios <= 0:
        raise ValueError("El número de usuarios debe ser mayor que 0")
    
    usuarios = []
    
    for i in range(num_usuarios):
        usuario = {
            'id': i + 1,
            'nombre': random.choice(NOMBRES),
            'edad': random.randint(18, 65),
            'puntuacion': round(random.uniform(0.0, 10.0), 1)
        }
        usuarios.append(usuario)
    
    return usuarios

def mostrar_usuarios(usuarios: List[Dict]) -> None:
    """
    Muestra los usuarios en formato legible.
    
    Args:
        usuarios (List[Dict]): Lista de usuarios a mostrar
    """
    for usuario in usuarios:
        print(f"ID: {usuario['id']:2} | "
              f"Nombre: {usuario['nombre']:8} | "
              f"Edad: {usuario['edad']:2} | "
              f"Puntuación: {usuario['puntuacion']:4.1f}")

def analizar_usuarios(usuarios: List[Dict]) -> None:
    """
    Realiza un análisis estadístico básico de los usuarios.
    
    Args:
        usuarios (List[Dict]): Lista de usuarios a analizar
    """
    if not usuarios:
        print("No hay usuarios para analizar.")
        return
    
    # Estadísticas de edad
    edades = [usuario['edad'] for usuario in usuarios]
    edad_promedio = sum(edades) / len(edades)
    edad_min = min(edades)
    edad_max = max(edades)
    
    # Estadísticas de puntuación
    puntuaciones = [usuario['puntuacion'] for usuario in usuarios]
    puntuacion_promedio = sum(puntuaciones) / len(puntuaciones)
    puntuacion_min = min(puntuaciones)
    puntuacion_max = max(puntuaciones)
    
    # Distribución de nombres
    nombres_count = {}
    for usuario in usuarios:
        nombre = usuario['nombre']
        nombres_count[nombre] = nombres_count.get(nombre, 0) + 1
    
    nombre_mas_comun = max(nombres_count.items(), key=lambda x: x[1])
    
    print(f"Total de usuarios: {len(usuarios)}")
    print(f"Edad - Promedio: {edad_promedio:.1f}, Mín: {edad_min}, Máx: {edad_max}")
    print(f"Puntuación - Promedio: {puntuacion_promedio:.1f}, Mín: {puntuacion_min:.1f}, Máx: {puntuacion_max:.1f}")
    print(f"Nombre más común: {nombre_mas_comun[0]} ({nombre_mas_comun[1]} veces)")

def generar_usuarios_avanzado(num_usuarios: int, semilla: int = None) -> List[Dict]:
    """
    Versión avanzada con control de semilla para reproducibilidad.
    
    Args:
        num_usuarios (int): Número de usuarios a generar
        semilla (int, optional): Semilla para reproducibilidad
        
    Returns:
        List[Dict]: Lista de diccionarios con datos de usuarios
    """
    if semilla is not None:
        random.seed(semilla)
    
    return generar_usuarios(num_usuarios)

# Ejemplo de uso independiente del módulo
if __name__ == "__main__":
    # Prueba básica del módulo
    print("=== PRUEBA DEL MÓDULO UTILS ===")
    usuarios_prueba = generar_usuarios(5)
    mostrar_usuarios(usuarios_prueba)
    print("\n--- Análisis ---")
    analizar_usuarios(usuarios_prueba)

