#Tema5: Organización del código con OOP

"""
Objetivo: Crear una clase Persona con atributos y un método para presentarse
Enunciado: Crea una clase llamada Persona con los siguientes elementos:

Un constructor __init__ que reciba como parámetros nombre y edad y los almacene como atributos de instancia.

Un método llamado presentarse que devuelva un string con el formato: "Hola, me llamo {nombre} y tengo {edad} 
años".

Luego, crea una instancia de la clase Persona con tu nombre y edad, y llama al método presentarse para 
verificar que funciona correctamente.
"""

# ===================================
# ARCHIVO: ejercicio_persona.py
# ===================================

class Persona:
    """
    Clase que representa a una persona con nombre y edad.
    """
    
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        
        Args:
            nombre (str): Nombre de la persona
            edad (int): Edad de la persona
        """
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        """
        Retorna un mensaje de presentación de la persona.
        
        Returns:
            str: Mensaje de presentación
        """
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"

# Crear una instancia con mis datos
mi_persona = Persona("Ana", 28)

# Llamar al método presentarse
mensaje_presentacion = mi_persona.presentarse()
print(mensaje_presentacion)
