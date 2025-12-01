#Tema5- Leccion 2

#Ejercicio: Practicando Self

"""Objetivo: Objetivo
Crear una clase con métodos que utilicen self para acceder a atributos de instancia

Enunciado:

Crea una clase llamada Libro con los siguientes requisitos:

El constructor debe inicializar tres atributos de instancia: titulo, autor y paginas.

Implementa un método llamado describir que devuelva un string con el formato: "[Titulo] escrito por [Autor] - [Paginas] páginas".

Implementa un método llamado es_largo que devuelva True si el libro tiene más de 300 páginas, y False en caso contrario.

Implementa un método llamado resumir que reciba un parámetro longitud y devuelva un string con el formato: "[Titulo] - Resumen de [longitud] caracteres". Si no se proporciona el parámetro longitud, debe usar un valor predeterminado de 50.

Prueba tu clase creando al menos dos instancias diferentes de Libro y llamando a todos sus métodos.
"""

"""
class Libro:
    def __init__(self, titulo, autor, paginas):
        # Inicializamos los atributos de instancia usando self
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def describir(self):
        # Usamos self para acceder a los atributos de instancia
        return f"'{self.titulo}' escrito por {self.autor} - {self.paginas} páginas"
    
    def es_largo(self):
        # Usamos self para acceder al atributo paginas
        return self.paginas > 300
    
    def resumir(self, longitud=50):
        # Usamos self para acceder al atributo titulo
        return f"'{self.titulo}' - Resumen de {longitud} caracteres"

# Probamos la clase creando instancias y llamando a los métodos
def main():
    # Crear dos instancias diferentes de Libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
    
    # Probar todos los métodos con el primer libro
    print("=== LIBRO 1 ===")
    print(libro1.describir())
    print(f"¿Es un libro largo? {libro1.es_largo()}")
    print(libro1.resumir())
    print(libro1.resumir(100))
    
    print("\n=== LIBRO 2 ===")
    # Probar todos los métodos con el segundo libro
    print(libro2.describir())
    print(f"¿Es un libro largo? {libro2.es_largo()}")
    print(libro2.resumir())
    print(libro2.resumir(30))
    
    # Demostración adicional
    print("\n=== DEMOSTRACIÓN ADICIONAL ===")
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    print(libro3.describir())
    print(f"¿Es un libro largo? {libro3.es_largo()}")
    print(f"Páginas exactas: {libro3.paginas}")

# Ejecutar las pruebas
if __name__ == "__main__":
    main()
"""


#Lección: Variables de clase y variables de instancia

#Ejercicio:

"""
Objetivo: Objetivo
Crear una clase con variables de clase e instancia para gestionar un sistema de biblioteca
Enunciado: Crea una clase llamada Biblioteca que gestione libros utilizando variables de clase e instancia 
adecuadamente.

La clase debe tener:

Una variable de clase total_libros inicializada en 0 que lleve la cuenta de todos los libros en el sistema.
Una variable de clase nombre_biblioteca con el valor "Biblioteca Central".
En el método __init__, recibe el parámetro nombre_seccion (por ejemplo "Ficción", "Historia", etc.) 
y crea una variable de instancia para almacenarlo.
En el método __init__, inicializa una variable de instancia libros como una lista vacía para almacenar 
los libros de esa sección.
Un método agregar_libro(self, titulo) que añada el título a la lista de libros de la sección e incremente 
la variable de clase total_libros.
Un método obtener_informe(self) que devuelva un string con el formato: "Sección [nombre_seccion] de 
[nombre_biblioteca]: [cantidad] libros".
Finalmente, crea dos instancias de la clase con diferentes secciones, agrega algunos libros a cada una y 
muestra sus informes para verificar que la variable de clase se comparte correctamente.
"""

class Biblioteca:
    # Variables de clase
    total_libros = 0
    nombre_biblioteca = "Biblioteca Central"
    
    def __init__(self, nombre_seccion):
        # Variables de instancia
        self.nombre_seccion = nombre_seccion
        self.libros = []  # Lista vacía para los libros de esta sección
    
    def agregar_libro(self, titulo):
        """Añade un libro a la sección e incrementa el contador total"""
        self.libros.append(titulo)
        Biblioteca.total_libros += 1
        return f"Libro '{titulo}' agregado a la sección {self.nombre_seccion}"
    
    def obtener_informe(self):
        """Devuelve un string con el informe de la sección"""
        cantidad = len(self.libros)
        return f"Sección {self.nombre_seccion} de {Biblioteca.nombre_biblioteca}: {cantidad} libros"
    
    def listar_libros(self):
        """Método adicional para listar los libros de la sección"""
        if not self.libros:
            return f"No hay libros en la sección {self.nombre_seccion}"
        
        libros_str = "\n".join(f"  - {libro}" for libro in self.libros)
        return f"Libros en {self.nombre_seccion}:\n{libros_str}"

# Crear instancias y probar la clase
def main():
    print("=== SISTEMA DE BIBLIOTECA ===\n")
    
    # Crear dos secciones diferentes
    seccion_ficcion = Biblioteca("Ficción")
    seccion_historia = Biblioteca("Historia")
    
    print("Estado inicial:")
    print(seccion_ficcion.obtener_informe())
    print(seccion_historia.obtener_informe())
    print(f"Total de libros en el sistema: {Biblioteca.total_libros}")
    
    print("\n=== AGREGANDO LIBROS A FICCIÓN ===")
    print(seccion_ficcion.agregar_libro("Cien años de soledad"))
    print(seccion_ficcion.agregar_libro("1984"))
    print(seccion_ficcion.agregar_libro("El Quijote"))
    
    print("\n=== AGREGANDO LIBROS A HISTORIA ===")
    print(seccion_historia.agregar_libro("Sapiens"))
    print(seccion_historia.agregar_libro("Breve historia del mundo"))
    
    print("\n=== INFORMES ACTUALIZADOS ===")
    print(seccion_ficcion.obtener_informe())
    print(seccion_historia.obtener_informe())
    print(f"Total de libros en el sistema: {Biblioteca.total_libros}")
    
    print("\n=== DETALLES POR SECCIÓN ===")
    print(seccion_ficcion.listar_libros())
    print()
    print(seccion_historia.listar_libros())
    
    # Demostración adicional
    print("\n=== CREANDO UNA TERCERA SECCIÓN ===")
    seccion_ciencia = Biblioteca("Ciencia")
    print(seccion_ciencia.agregar_libro("Breve historia del tiempo"))
    print(seccion_ciencia.agregar_libro("El gen egoísta"))
    print(seccion_ciencia.obtener_informe())
    print(f"Total de libros en el sistema: {Biblioteca.total_libros}")

# Ejecutar las pruebas
if __name__ == "__main__":
    main()
    
    
#Lección Métodos dentro de Clases

#Ejercicio: Ejercicio comportamiento con métodos

    """
    Objetivo: Implementar una clase Contador con métodos de instancia, clase y estáticos
    Enunciado:
    
    Crea una clase llamada Contador que gestione un valor numérico. La clase debe implementar:

Un atributo de clase contadores_creados que lleve la cuenta de cuántas instancias se han creado.

Un método de instancia incrementar() que aumente el valor del contador en 1 y devuelva el nuevo valor.

Un método de instancia decrementar() que disminuya el valor del contador en 1 y devuelva el nuevo valor. El contador nunca debe ser negativo.

Un método de clase @classmethod llamado reiniciar_contador_global() que ponga a cero el contador de instancias creadas.

Un método estático @staticmethod llamado es_par(numero) que devuelva True si el número proporcionado es par, o False en caso contrario.

Puedes empezar con este esquema:

class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0
    
    def __init__(self, valor_inicial=0):
        # Completa el constructor
        pass
        
    # Implementa los métodos requeridos
"""

"""
class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0
    
    def __init__(self, valor_inicial=0):
        # Variable de instancia para el valor del contador
        self.valor = valor_inicial
        
        # Incrementar el contador de clase
        Contador.contadores_creados += 1
    
    def incrementar(self):
        """Método de instancia: aumenta el valor en 1 y devuelve el nuevo valor"""
        self.valor += 1
        return self.valor
    
    def decrementar(self):
        """Método de instancia: disminuye el valor en 1, nunca negativo"""
        if self.valor > 0:
            self.valor -= 1
        return self.valor
    
    @classmethod
    def reiniciar_contador_global(cls):
        """Método de clase: reinicia el contador de instancias creadas"""
        contadores_anteriores = cls.contadores_creados
        cls.contadores_creados = 0
        return f"Contador global reiniciado. Había {contadores_anteriores} instancias."
    
    @staticmethod
    def es_par(numero):
        """Método estático: verifica si un número es par"""
        return numero % 2 == 0
    
    # Métodos adicionales para mejor usabilidad
    def __str__(self):
        """Representación legible del contador"""
        return f"Contador: {self.valor}"
    
    def __repr__(self):
        """Representación técnica del contador"""
        return f"Contador(valor={self.valor})"

# === PRUEBA COMPLETA DEL SISTEMA ===
def main():
    print("=== SISTEMA DE CONTADORES ===\n")
    
    # Crear algunos contadores
    print("1. Creando contadores...")
    contador1 = Contador(5)
    contador2 = Contador(10)
    contador3 = Contador()  # Valor por defecto 0
    
    print(f"Contadores creados: {Contador.contadores_creados}")
    print(f"Contador 1: {contador1}")
    print(f"Contador 2: {contador2}")
    print(f"Contador 3: {contador3}")
    
    # Probar métodos de instancia - incrementar
    print("\n2. Probando método incrementar():")
    print(f"Contador1 antes: {contador1.valor}")
    print(f"Contador1 incrementar(): {contador1.incrementar()}")
    print(f"Contador1 incrementar(): {contador1.incrementar()}")
    print(f"Contador1 después: {contador1.valor}")
    
    # Probar métodos de instancia - decrementar
    print("\n3. Probando método decrementar():")
    print(f"Contador2 antes: {contador2.valor}")
    print(f"Contador2 decrementar(): {contador2.decrementar()}")
    print(f"Contador2 decrementar(): {contador2.decrementar()}")
    print(f"Contador2 después: {contador2.valor}")
    
    # Probar que no puede ser negativo
    print("\n4. Probando protección contra valores negativos:")
    print(f"Contador3 antes: {contador3.valor}")
    for i in range(3):
        resultado = contador3.decrementar()
        print(f"Intento {i+1}: decrementar() = {resultado}")
    
    # Probar método estático
    print("\n5. Probando método estático es_par():")
    numeros_prueba = [2, 5, 10, 15, 0, -4, -7]
    for num in numeros_prueba:
        resultado = Contador.es_par(num)
        print(f"¿{num} es par? {resultado}")
    
    # También se puede llamar desde una instancia
    print(f"\nDesde instancia - ¿{contador1.valor} es par? {contador1.es_par(contador1.valor)}")
    
    # Probar método de clase
    print("\n6. Probando método de clase reiniciar_contador_global():")
    print(f"Contadores creados antes: {Contador.contadores_creados}")
    resultado_reinicio = Contador.reiniciar_contador_global()
    print(resultado_reinicio)
    print(f"Contadores creados después: {Contador.contadores_creados}")
    
    # Crear más contadores después del reinicio
    print("\n7. Creando nuevos contadores después del reinicio:")
    contador4 = Contador(100)
    contador5 = Contador(200)
    print(f"Nuevos contadores creados: {Contador.contadores_creados}")
    print(f"Contador4: {contador4}")
    print(f"Contador5: {contador5}")
    
    # Demostración adicional de todos los métodos trabajando juntos
    print("\n8. Demostración completa:")
    demo = Contador(7)
    print(f"Contador demo: {demo}")
    
    # Usar métodos de instancia
    demo.incrementar()
    demo.incrementar()
    demo.decrementar()
    print(f"Después de operaciones: {demo}")
    
    # Usar método estático con el valor actual
    print(f"¿El valor actual ({demo.valor}) es par? {Contador.es_par(demo.valor)}")
    
    # Ver estadísticas globales
    print(f"Total de contadores creados en el sistema: {Contador.contadores_creados}")

# Ejecutar las pruebas
if __name__ == "__main__":
    main()
"""

#Lección: Herencias

#Ejercicio: Ejercicio de herencia

"""Objetivo
Crear una jerarquía de clases para modelar diferentes tipos de vehículos

Enunciado:Crea una jerarquía de clases para modelar vehículos. Debes implementar:

Una clase base Vehiculo con los siguientes atributos y métodos:
Atributos: marca, modelo y año
Un método mostrar_info() que devuelva un string con la información básica del vehículo
Una clase derivada Automovil que herede de Vehiculo y añada:
Un atributo adicional puertas (número de puertas)
Sobrescribe el método mostrar_info() para incluir el número de puertas
Una clase derivada Motocicleta que herede de Vehiculo y añada:
Un atributo adicional cilindrada (en cc)
Sobrescribe el método mostrar_info() para incluir la cilindrada
Finalmente, crea una instancia de cada clase derivada y muestra su información usando el método mostrar_info().
"""
"""
#Solución:

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año})"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        # Llamamos al constructor de la clase base
        super().__init__(marca, modelo, año)
        # Añadimos el atributo específico de Automovil
        self.puertas = puertas
    
    def mostrar_info(self):
        # Obtenemos la información base del vehículo
        info_base = super().mostrar_info()
        # Añadimos la información específica del automóvil
        return f"{info_base} - {self.puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        # Llamamos al constructor de la clase base
        super().__init__(marca, modelo, año)
        # Añadimos el atributo específico de Motocicleta
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        # Obtenemos la información base del vehículo
        info_base = super().mostrar_info()
        # Añadimos la información específica de la motocicleta
        return f"{info_base} - {self.cilindrada}cc"

# === CREACIÓN DE INSTANCIAS Y PRUEBAS ===
def main():
    print("=== SISTEMA DE VEHÍCULOS ===\n")
    
    # Crear una instancia de Automovil
    mi_auto = Automovil("Toyota", "Corolla", 2022, 4)
    
    # Crear una instancia de Motocicleta
    mi_moto = Motocicleta("Yamaha", "MT-07", 2023, 689)
    
    # Mostrar información de los vehículos
    print("Información del Automóvil:")
    print(mi_auto.mostrar_info())
    
    print("\nInformación de la Motocicleta:")
    print(mi_moto.mostrar_info())
    
    # Demostración adicional con más vehículos
    print("\n=== MÁS VEHÍCULOS ===")
    
    # Crear más automóviles
    auto_deportivo = Automovil("Porsche", "911", 2024, 2)
    auto_familiar = Automovil("Honda", "CR-V", 2023, 5)
    
    # Crear más motocicletas
    moto_deportiva = Motocicleta("Kawasaki", "Ninja ZX-6R", 2024, 636)
    moto_custom = Motocicleta("Harley-Davidson", "Street Glide", 2023, 1868)
    
    # Mostrar información de todos los vehículos
    vehiculos = [auto_deportivo, auto_familiar, moto_deportiva, moto_custom]
    
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Vehículo {i}: {vehiculo.mostrar_info()}")

# Ejecutar las pruebas
if __name__ == "__main__":
    main()
    """
    
#Lección: Composición

#Ejercicio: Ejercicio de composición

"""Objetivo: Objetivo
Crear un sistema de biblioteca usando composición en Python
Enunciado: 
"""

"""
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def contiene_titulo(self, texto_busqueda):
        """Delega la búsqueda al propio libro"""
        return texto_busqueda.lower() in self.titulo.lower()
    
    def es_del_autor(self, autor_busqueda):
        """Delega la verificación del autor al propio libro"""
        return autor_busqueda.lower() in self.autor.lower()
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.año_publicacion})"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        # COMPOSICIÓN: La biblioteca "tiene una" colección de libros
        self.libros = []
    
    def agregar_libro(self, libro):
        """Agrega un nuevo libro a la colección"""
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado a la biblioteca"
    
    def buscar_por_titulo(self, texto_busqueda):
        """
        Busca libros que contengan el texto en el título
        DELEGA la búsqueda a cada objeto Libro
        """
        resultados = []
        for libro in self.libros:
            # Delegación: cada libro verifica si contiene el texto
            if libro.contiene_titulo(texto_busqueda):
                resultados.append(libro)
        return resultados
    
    def contar_libros_autor(self, autor_busqueda):
        """
        Cuenta cuántos libros hay de un autor específico
        DELEGA la verificación del autor a cada objeto Libro
        """
        contador = 0
        for libro in self.libros:
            # Delegación: cada libro verifica si es del autor
            if libro.es_del_autor(autor_busqueda):
                contador += 1
        return contador
    
    def mostrar_todos_libros(self):
        """Muestra todos los libros en la biblioteca"""
        if not self.libros:
            return "La biblioteca está vacía"
        
        resultado = f"Libros en {self.nombre}:\n"
        for i, libro in enumerate(self.libros, 1):
            resultado += f"{i}. {libro}\n"
        return resultado
    
    def __str__(self):
        return f"Biblioteca: {self.nombre} ({len(self.libros)} libros)"

# === PRUEBA DEL SISTEMA ===
def main():
    print("=== SISTEMA DE BIBLIOTECA CON COMPOSICIÓN ===\n")
    
    # Crear la biblioteca
    biblioteca = Biblioteca("Biblioteca Central")
    print(f"✅ {biblioteca} creada\n")
    
    # Crear algunos libros
    libros_a_agregar = [
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985),
        Libro("1984", "George Orwell", 1949),
        Libro("Rebelión en la granja", "George Orwell", 1945),
        Libro("El principito", "Antoine de Saint-Exupéry", 1943),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
        Libro("La ciudad y los perros", "Mario Vargas Llosa", 1963),
        Libro("Cien años de soledad: Edición especial", "Gabriel García Márquez", 2007)
    ]
    
    # Agregar libros a la biblioteca
    print("📚 AGREGANDO LIBROS:")
    for libro in libros_a_agregar:
        print(f"  {biblioteca.agregar_libro(libro)}")
    
    print(f"\n{biblioteca}")
    
    # Probar búsqueda por título
    print("\n🔍 BÚSQUEDA POR TÍTULO:")
    busquedas = ["cien", "años", "granja", "principito", "python"]
    
    for busqueda in busquedas:
        resultados = biblioteca.buscar_por_titulo(busqueda)
        print(f"\nBuscando '{busqueda}':")
        if resultados:
            for libro in resultados:
                print(f"  ✅ {libro}")
        else:
            print(f"  ❌ No se encontraron libros con '{busqueda}'")
    
    # Probar conteo por autor
    print("\n👤 CONTEO POR AUTOR:")
    autores = ["García Márquez", "Orwell", "Cervantes", "Borges"]
    
    for autor in autores:
        cantidad = biblioteca.contar_libros_autor(autor)
        print(f"  {autor}: {cantidad} libro(s)")
    
    # Mostrar todos los libros
    print(f"\n{biblioteca.mostrar_todos_libros()}")

# === PRUEBA ADICIONAL CON MÁS FUNCIONALIDADES ===
def prueba_avanzada():
    print("\n" + "="*60)
    print("PRUEBA AVANZADA")
    print("="*60)
    
    # Crear una nueva biblioteca especializada
    biblioteca_ciencia = Biblioteca("Biblioteca de Ciencia y Tecnología")
    
    # Agregar libros de ciencia
    libros_ciencia = [
        Libro("Breve historia del tiempo", "Stephen Hawking", 1988),
        Libro("El gen egoísta", "Richard Dawkins", 1976),
        Libro("Sapiens: De animales a dioses", "Yuval Noah Harari", 2011),
        Libro("Homo Deus: Breve historia del mañana", "Yuval Noah Harari", 2015),
        Libro("El origen de las especies", "Charles Darwin", 1859),
        Libro("Python Crash Course", "Eric Matthes", 2015),
        Libro("Clean Code", "Robert C. Martin", 2008),
        Libro("The Pragmatic Programmer", "Andrew Hunt", 1999)
    ]
    
    print("📚 Configurando biblioteca de ciencia:")
    for libro in libros_ciencia:
        biblioteca_ciencia.agregar_libro(libro)
    
    print(f"\n{biblioteca_ciencia}")
    
    # Búsquedas específicas
    print("\n🔍 Búsquedas en biblioteca de ciencia:")
    
    # Buscar por tema
    temas = ["historia", "python", "code", "homo"]
    for tema in temas:
        resultados = biblioteca_ciencia.buscar_por_titulo(tema)
        print(f"\nLibros sobre '{tema}':")
        for libro in resultados:
            print(f"  📖 {libro}")
    
    # Contar por autor
    print("\n👤 Autores más populares:")
    autores_ciencia = ["Harari", "Hawking", "Darwin", "Martin"]
    for autor in autores_ciencia:
        cantidad = biblioteca_ciencia.contar_libros_autor(autor)
        print(f"  {autor}: {cantidad} libro(s)")

# Ejecutar ambas pruebas
if __name__ == "__main__":
    main()
    prueba_avanzada()
"""

#Lección: Módulos y Paquetes    

"""
Ejercicio: Ejercicio crear y usar módulos

Objetivo: Crear un módulo de utilidades matemáticas y aprende a importarlo
Enunciado: Escribe el código para un módulo llamado operaciones_matematicas.py que contenga las siguientes funciones:

sumar(a, b): Devuelve la suma de dos números
restar(a, b): Devuelve la resta de dos números
multiplicar(a, b): Devuelve el producto de dos números
dividir(a, b): Devuelve la división de a entre b (debe manejar la división por cero devolviendo un mensaje de error)
Además, define una constante PI con el valor 3.14159.

Luego, escribe el código para un archivo principal calculadora.py que importe el módulo que has creado y realice las siguientes operaciones:

Importa todas las funciones y la constante PI del módulo
Calcula y muestra el resultado de sumar 15 y 7
Calcula y muestra el resultado de multiplicar 3.5 por 2
Calcula y muestra el área de un círculo con radio 5 utilizando la constante PI
Escribe el código python directamente en el editor, no es necesario crear archivos, escribe el código todo seguido en el propio editor.

"""

# operaciones_matematicas.py

## Definición de la constante PI
PI = 3.14159

## Función para sumar dos números
def sumar(a, b):
    return a + b

## Función para restar dos números
def restar(a, b):
    return a - b

## Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

## Función para dividir dos números, manejando división por cero
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


# calculadora.py

## Importar todas las funciones y la constante PI del módulo
from operaciones_matematicas import sumar, restar, multiplicar, dividir, PI

## Calcular y mostrar el resultado de sumar 15 y 7
resultado_suma = sumar(15, 7)
print(f"15 + 7 = {resultado_suma}")

## Calcular y mostrar el resultado de multiplicar 3.5 por 2
resultado_multiplicacion = multiplicar(3.5, 2)
print(f"3.5 × 2 = {resultado_multiplicacion}")

## Calcular y mostrar el área de un círculo con radio 5
radio = 5
area_circulo = multiplicar(PI, multiplicar(radio, radio))
print(f"Área del círculo con radio 5 = {area_circulo}")

## Demostración adicional de las funciones restar y dividir
print(f"20 - 8 = {restar(20, 8)}")
print(f"10 / 2 = {dividir(10, 2)}")
print(f"10 / 0 = {dividir(10, 0)}")