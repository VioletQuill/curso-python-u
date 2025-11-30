#Lección 3- Ejercicio 1: Argumentos opcionales y flexibles con *args y **kwards

"""
Objetivo: Crear una función que utilice *args y **kwargs para procesar datos de estudiantes

Enunciado: Crea una función llamada procesar_estudiantes que reciba un parámetro obligatorio escuela (string) 
seguido de un número variable de nombres de estudiantes como argumentos posicionales (*args) y datos adicionales 
como argumentos con nombre (**kwargs).

La función debe:

Devolver un diccionario con la siguiente estructura:
Una clave 'escuela' con el valor del parámetro obligatorio
Una clave 'estudiantes' con la lista de nombres recibidos en *args
Una clave 'datos_adicionales' con un diccionario que contenga todos los argumentos con nombre recibidos
Ejemplo de uso:

resultado = procesar_estudiantes("IES Tecnológico", "Ana", 
"Carlos", "Elena", curso="1º DAW", turno="mañana")

print(resultado)

# Debería imprimir:
# {'escuela': 'IES Tecnológico', 'estudiantes': ['Ana',
# 'Carlos', 'Elena'], 'datos_adicionales': {'curso': '1º DAW', 'turno': 'mañana'}}
"""

# ===================================
# ARCHIVO: ejercicio_estudiantes_mejorado.py
# ===================================

def procesar_estudiantes(escuela, *args, **kwargs):
    """
    Procesa datos de estudiantes con argumentos flexibles y validaciones.
    
    Args:
        escuela (str): Nombre de la escuela (obligatorio)
        *args: Nombres de estudiantes como argumentos posicionales
        **kwargs: Datos adicionales como argumentos con nombre
    
    Returns:
        dict: Diccionario con escuela, estudiantes y datos adicionales
    
    Raises:
        ValueError: Si la escuela está vacía o no hay estudiantes
    """
    # Validaciones
    if not escuela or not isinstance(escuela, str):
        raise ValueError("El parámetro 'escuela' es obligatorio y debe ser un string")
    
    if not args:
        raise ValueError("Se requiere al menos un estudiante")
    
    # Convertir args a lista y validar que todos sean strings
    estudiantes = []
    for estudiante in args:
        if not isinstance(estudiante, str):
            raise ValueError(f"Todos los estudiantes deben ser strings. Recibido: {type(estudiante)}")
        estudiantes.append(estudiante)
    
    return {
        'escuela': escuela,
        'estudiantes': estudiantes,
        'datos_adicionales': kwargs
    }

# Función para mostrar resultados de forma legible
def mostrar_resultado(resultado):
    """Muestra el resultado de forma formateada."""
    print("\n" + "="*50)
    print("RESULTADO DEL PROCESAMIENTO DE ESTUDIANTES")
    print("="*50)
    print(f"Escuela: {resultado['escuela']}")
    print(f"Estudiantes: {', '.join(resultado['estudiantes'])}")
    print(f"Total de estudiantes: {len(resultado['estudiantes'])}")
    
    if resultado['datos_adicionales']:
        print("\nDatos adicionales:")
        for clave, valor in resultado['datos_adicionales'].items():
            print(f"  - {clave}: {valor}")
    else:
        print("\nNo hay datos adicionales")
    print("="*50)

# Ejemplos de uso
def main():
    """Función principal con ejemplos de uso."""
    
    print("=== SISTEMA DE PROCESAMIENTO DE ESTUDIANTES ===\n")
    
    # Ejemplo 1: Caso del enunciado
    print("1. Ejemplo del enunciado:")
    resultado1 = procesar_estudiantes(
        "IES Tecnológico", 
        "Ana", "Carlos", "Elena", 
        curso="1º DAW", 
        turno="mañana"
    )
    mostrar_resultado(resultado1)
    
    # Ejemplo 2: Más estudiantes y datos
    print("\n2. Ejemplo con más datos:")
    resultado2 = procesar_estudiantes(
        "Colegio Santa María",
        "Laura", "Miguel", "Sofía", "David", "Elena",
        nivel="Bachillerato",
        especialidad="Ciencias",
        año_academico="2024-2025",
        director="Dr. García"
    )
    mostrar_resultado(resultado2)
    
    # Ejemplo 3: Sin datos adicionales
    print("\n3. Ejemplo sin datos adicionales:")
    resultado3 = procesar_estudiantes(
        "Academia de Idiomas",
        "Pedro", "María", "Juan"
    )
    mostrar_resultado(resultado3)
    
    # Ejemplo 4: Con muchos datos adicionales
    print("\n4. Ejemplo con información completa:")
    resultado4 = procesar_estudiantes(
        "Escuela de Música",
        "Carlos", "Ana", "Luis", "Marta", "Javier",
        instrumento_principal="Piano",
        nivel="Avanzado",
        horario="Tardes",
        profesor="Sr. Rodríguez",
        sala="Aula 301",
        actividades=["Concierto mensual", "Taller de teoría"],
        beca=True
    )
    mostrar_resultado(resultado4)

# Pruebas de validación
def pruebas_validacion():
    """Pruebas de las validaciones de la función."""
    print("\n=== PRUEBAS DE VALIDACIÓN ===")
    
    try:
        # Prueba 1: Escuela vacía
        procesar_estudiantes("", "Ana", "Carlos")
    except ValueError as e:
        print(f"✓ Prueba 1 pasada: {e}")
    
    try:
        # Prueba 2: Sin estudiantes
        procesar_estudiantes("IES Ejemplo")
    except ValueError as e:
        print(f"✓ Prueba 2 pasada: {e}")
    
    try:
        # Prueba 3: Estudiante no string
        procesar_estudiantes("IES Ejemplo", "Ana", 123, "Carlos")
    except ValueError as e:
        print(f"✓ Prueba 3 pasada: {e}")
    
    print("Todas las validaciones funcionan correctamente ✓")

# Ejecutar el programa
if __name__ == "__main__":
    main()
    pruebas_validacion()