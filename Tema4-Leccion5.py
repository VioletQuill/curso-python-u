#Tema 4- Lección 5 Librería standard: módulo sys, logging, os

"""
Objetivo: Crear un script que liste archivos por tamaño en un directorio
Enunciado: 
Crea un script en Python que utilice el módulo os para listar todos los archivos (no directorios) en el directorio actual, ordenados por tamaño (de mayor a menor). Para cada archivo, muestra su nombre y tamaño en bytes.

El script debe:

Obtener la lista de todos los elementos en el directorio actual
Filtrar solo los archivos (no directorios)
Obtener el tamaño de cada archivo usando las funciones apropiadas
Ordenar la lista de archivos por tamaño de forma descendente
Mostrar el nombre y tamaño de cada archivo
Puedes empezar importando el módulo os y utilizando os.listdir() para obtener los elementos del directorio actual.

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
# ===================================
# ARCHIVO 1: main.py
# ===================================

from utils import listar_archivos_por_tamaño, formatear_tamaño

def main():
    """Función principal del script."""
    print("=== LISTADOR DE ARCHIVOS POR TAMAÑO ===\n")
    
    try:
        # Obtener y mostrar archivos ordenados por tamaño
        archivos_ordenados = listar_archivos_por_tamaño()
        
        if not archivos_ordenados:
            print("No se encontraron archivos en el directorio actual.")
            return
        
        print(f"Archivos en el directorio actual (ordenados por tamaño):")
        print("-" * 50)
        
        for archivo, tamaño in archivos_ordenados:
            tamaño_formateado = formatear_tamaño(tamaño)
            print(f"{archivo:<30} {tamaño:>10} bytes ({tamaño_formateado})")
        
        # Mostrar estadísticas
        total_archivos = len(archivos_ordenados)
        tamaño_total = sum(tamaño for _, tamaño in archivos_ordenados)
        
        print("-" * 50)
        print(f"Total: {total_archivos} archivos, {tamaño_total:,} bytes ({formatear_tamaño(tamaño_total)})")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
# ===================================
# ARCHIVO 2: utils.py
# ===================================

import os
from pathlib import Path

def listar_archivos_por_tamaño(directorio="."):
    """
    Lista todos los archivos en un directorio ordenados por tamaño (de mayor a menor).
    
    Args:
        directorio (str): Ruta del directorio a analizar (por defecto directorio actual)
    
    Returns:
        list: Lista de tuplas (nombre_archivo, tamaño_bytes) ordenada por tamaño descendente
    """
    try:
        # Obtener la lista de todos los elementos en el directorio
        elementos = os.listdir(directorio)
        
        archivos_con_tamaño = []
        
        for elemento in elementos:
            ruta_completa = os.path.join(directorio, elemento)
            
            # Filtrar solo archivos (no directorios)
            if os.path.isfile(ruta_completa):
                try:
                    # Obtener el tamaño del archivo
                    tamaño = os.path.getsize(ruta_completa)
                    archivos_con_tamaño.append((elemento, tamaño))
                except (OSError, IOError) as e:
                    # Si no se puede acceder al archivo, continuar con el siguiente
                    print(f"Advertencia: No se pudo acceder a '{elemento}': {e}")
                    continue
        
        # Ordenar por tamaño de forma descendente
        archivos_con_tamaño.sort(key=lambda x: x[1], reverse=True)
        
        return archivos_con_tamaño
        
    except FileNotFoundError:
        raise FileNotFoundError(f"El directorio '{directorio}' no existe")
    except PermissionError:
        raise PermissionError(f"No tienes permisos para acceder al directorio '{directorio}'")
    except Exception as e:
        raise Exception(f"Error al listar archivos: {e}")

def formatear_tamaño(tamaño_bytes):
    """
    Convierte un tamaño en bytes a un formato legible (KB, MB, GB).
    
    Args:
        tamaño_bytes (int): Tamaño en bytes
    
    Returns:
        str: Tamaño formateado en la unidad apropiada
    """
    if tamaño_bytes == 0:
        return "0 B"
    
    unidades = ['B', 'KB', 'MB', 'GB', 'TB']
    tamaño = float(tamaño_bytes)
    
    for unidad in unidades:
        if tamaño < 1024.0 or unidad == 'TB':
            if unidad == 'B':
                return f"{tamaño:.0f} {unidad}"
            else:
                return f"{tamaño:.2f} {unidad}"
        tamaño /= 1024.0

# Función adicional para usar pathlib (enfoque moderno)
def listar_archivos_por_tamaño_pathlib(directorio="."):
    """
    Versión alternativa usando pathlib para listar archivos por tamaño.
    
    Args:
        directorio (str): Ruta del directorio a analizar
    
    Returns:
        list: Lista de tuplas (nombre_archivo, tamaño_bytes) ordenada por tamaño descendente
    """
    directorio_path = Path(directorio)
    
    if not directorio_path.exists():
        raise FileNotFoundError(f"El directorio '{directorio}' no existe")
    
    if not directorio_path.is_dir():
        raise ValueError(f"'{directorio}' no es un directorio")
    
    archivos_con_tamaño = []
    
    for elemento in directorio_path.iterdir():
        if elemento.is_file():
            try:
                tamaño = elemento.stat().st_size
                archivos_con_tamaño.append((elemento.name, tamaño))
            except (OSError, IOError) as e:
                print(f"Advertencia: No se pudo acceder a '{elemento.name}': {e}")
                continue
    
    # Ordenar por tamaño de forma descendente
    archivos_con_tamaño.sort(key=lambda x: x[1], reverse=True)
    
    return archivos_con_tamaño

# Ejemplo de uso independiente del módulo
if __name__ == "__main__":
    # Prueba básica del módulo
    print("=== PRUEBA DEL MÓDULO UTILS ===")
    try:
        archivos = listar_archivos_por_tamaño()
        print(f"Encontrados {len(archivos)} archivos:")
        for archivo, tamaño in archivos[:5]:  # Mostrar solo los 5 primeros
            print(f"  {archivo}: {formatear_tamaño(tamaño)}")
    except Exception as e:
        print(f"Error: {e}")