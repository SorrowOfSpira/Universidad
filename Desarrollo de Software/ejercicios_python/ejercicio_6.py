"""
Ejercicio 6

Cree un programa con las siguientes características:
a-  Crea una clase llamada “Libro” con los siguientes atributos:	
            --titulo
            --autor
            --año
            --genero
b-  Utiliza la el método __init__ para inicializar los atributos
c-  Agrega un método llamado obtener_info() que devuelva una cadena con algún formato para los detalles del libro (titulo, autor, año,  género).

d-  Agrega un método es_clasico() que devuelva True si el libro se publicó hace más de 50 años (basado en el año actual) y False en caso contrario.
e-  Crear objetos:
i       Instanciar al menos dos libros con diferentes atributos.
ii      Llama al método obtener_info() de cada libro para mostrar sus detalles.
iii     Llama al método es_clasico() de cada libro e imprimir si cada libro es un clásico.

Para determinar el año actual pueden solicitarlo al comenzar el programa o bien obtenerlo utilizando el módulo datetime.

Ejemplo:
from datetime import date
hoy = date.today()
print(f“Año actual: {hoy.year}”) # muestra: 2024
"""
from datetime import date
hoy = date.today()

class Libro:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

# Método de la clase
    def mostrar_atributos(self):
        print("---------------------------------")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Anio: {self.anio}")
        print(f"Genero : {self.genero}")

    def es_clasico(self):
        if ((hoy.year-self.anio) > 49):
            print(f"--{self.titulo} es clasico")
        else:
            print(f"--{self.titulo} no es clasico")
    
l1 = Libro(
    "Cyberpunk",
    "Marcin Przybyłowicz",
    2077,
    "Espionaje"
)
l2 = Libro(
    titulo="Cien años de soledad",
    autor="Gabriel García Márquez",
    anio=1967,
    genero="Realismo mágico"
)
l3 = Libro(
    titulo="1984",
    autor="George Orwell",
    anio=1949,
    genero="Distopía"
)

l1.mostrar_atributos()
l2.mostrar_atributos()
l3.mostrar_atributos()
l1.es_clasico()
l2.es_clasico()
l3.es_clasico()

