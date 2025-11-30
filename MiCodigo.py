#Identificadores válidos
mi_variable = 10
_variable2 = "Hola"
MiClase = type('MiClase', (), {})
def mi_funcion():
    pass
CONSTANTE = 3.14

print(mi_variable, _variable2, MiClase, CONSTANTE)

#Palabras reservadas (no válidos como identificadores)
# def = 5           
# class = "Texto"
# if = True
# return = None
# import = "Módulo"
# while = 10
# for = 20
# try = "Intentar"
# else = "Otro"
# with = "Con"
# print("¡Hola, mundo!")
print("¡Hola, mundo!")

#Comentarios

"""Ejemplo de comentario de bloque con comillas triples """
   
'''Este es otro Ejemplo de comentario de bloque con comillas simples
    Todas las líneas pertenecen al comentario de bloque.'''
    
# Comentario de una sola línea
# Este es un comentario de una sola línea

#Sangría
#Python no utiliza llaves para definir bloques de código, sino que depende de la sangría.
if mi_variable > 5:
    print("La variable es mayor que 5")
    if _variable2 == "Hola":
        print("La variable2 es igual a 'Hola'")
        
# La siguiente línea causaría un error de indentación si se descomentara
#print("Esto causará un error de indentación")

#Ejemplo de una sangría

variable = 1

if (variable == 1):
    print("Aquí pongo el código a ejecutar si la condición es verdadera")
    print ("Tiene una sangría de 4 espacios")