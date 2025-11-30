# Tema 4 - Lección : Creación de funciones, parámetros, argumentos, retorno

"""
# Objetivo: Crear una función que calcule el área de un rectángulo

Enunciado: Crea una función llamada calcular_area_rectangulo que reciba dos parámetros: base y altura. La función debe calcular y 
retornar el área del rectángulo (base × altura).

Luego, llama a la función con los valores 5 y 3, y almacena el resultado en una variable llamada area. Finalmente, imprime el 
resultado con un mensaje descriptivo.
"""
# ===================================
# ARCHIVO: ejercicio_rectangulo_interactivo.py
# ===================================

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def main():
    """Función principal del programa."""
    print("=== CALCULADORA DE ÁREA DE RECTÁNGULO ===\n")
    
    try:
        # Solicitar datos al usuario
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        
        # Calcular área
        area = calcular_area_rectangulo(base, altura)
        
        # Mostrar resultado
        print(f"\nEl área del rectángulo con base {base} y altura {altura} es: {area}")
        
        # Ejemplo adicional del enunciado
        print(f"\n--- Ejemplo del enunciado ---")
        area_ejemplo = calcular_area_rectangulo(5, 3)
        print(f"Base: 5, Altura: 3 → Área: {area_ejemplo}")
        
    except ValueError:
        print("Error: Por favor ingresa números válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
    
# Tema 4 - Lección : Creación de funciones, parámetros, argumentos, retorno

"""
# Objetivo: Crear una función que calcule el área de un rectángulo

Enunciado: Crea una función llamada calcular_area_rectangulo que reciba dos parámetros: base y altura. La función debe calcular y 
retornar el área del rectángulo (base × altura).

Luego, llama a la función con los valores 5 y 3, y almacena el resultado en una variable llamada area. Finalmente, imprime el 
resultado con un mensaje descriptivo.
"""
# ===================================
# ARCHIVO: ejercicio_rectangulo_interactivo.py
# ===================================

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def main():
    """Función principal del programa."""
    print("=== CALCULADORA DE ÁREA DE RECTÁNGULO ===\n")
    
    try:
        # Solicitar datos al usuario
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        
        # Calcular área
        area = calcular_area_rectangulo(base, altura)
        
        # Mostrar resultado
        print(f"\nEl área del rectángulo con base {base} y altura {altura} es: {area}")
        
        # Ejemplo adicional del enunciado
        print(f"\n--- Ejemplo del enunciado ---")
        area_ejemplo = calcular_area_rectangulo(5, 3)
        print(f"Base: 5, Altura: 3 → Área: {area_ejemplo}")
        
    except ValueError:
        print("Error: Por favor ingresa números válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
