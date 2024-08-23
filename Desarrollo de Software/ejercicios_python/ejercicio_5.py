"""
Ejercicio 5

Escriba un programa que permita crear una lista de 5 películas. 
El programa debe solicitar uno por uno los nombres de las películas junto con su año de estreno. 
Al finalizar la carga de datos, se deberá mostrar por pantalla una lista con los nombres de las películas ordenadas por nombre 
y un diccionario donde las claves sean los años de estreno y los valores sean las películas estrenadas ese año.

Ejemplo:
…
Ingrese nombre de pelicula: Batman inicia
Ingrese año de estreno: 2008
Resultado: 
[“300”, “Avatar”, “Batman Inicia”, “Iron Man”, “Tropic Thunder”]
{2005: “Batman Inicia”, 2006: “300”, 2008: “Tropic Thunder”, “Iron Man”}


"""
def agrupar_peliculas_por_anio(lista_peliculas):
    diccionario_peliculas = {}

    for nombre, anio in lista_peliculas:
        if anio in diccionario_peliculas:#  Si el año esta en el diccionario solo hace append del nombre de la pelicula en el año correspondiente
            diccionario_peliculas[anio].append(nombre)
        else:                            #  Si el año no está en el diccionario, se crea una entrada en el diccionario con el año como clave
            diccionario_peliculas[anio] = [nombre]
    
    return diccionario_peliculas




peliculas = []

for i in range(5):
        nombre = input(f"Ingrese nombre de la película {i + 1}: ")
        anio = int(input(f"Ingrese año de estreno de '{nombre}': "))
        peliculas.append((nombre, anio))#       al usar append, agrego al arreglo peliculas una tupla de la forma (nombre,anio)

peliculas_ordenadas = sorted(peliculas)#        Sorted ordena por el primer parametro, en caso de empate ordena por el segundo
print(f"\nLa lista ordenada queda de la siguiente manera")
print(peliculas_ordenadas)


# Crear el diccionario agrupado por año
diccionario = agrupar_peliculas_por_anio(peliculas_ordenadas)
print(f"\nEl diccionario queda de la siguiente manera")
print(diccionario)



