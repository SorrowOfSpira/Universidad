"""
Ejercicio 4
Escriba un programa que permita hacer la conversión de valores de temperatura entre Celsius y Fahrenheit. 
Se debe solicitar al usuario que ingrese un valor numérico y la escala original.
El programa deberá mostrar por pantalla el valor convertido incluyendo la escala final. Ver input(). 
Construya dos funciones, una para convertir datos a escala Celsius y otra para convertir los datos a escala Fahrenheit.

Ejemplo:
Ingrese temperatura: 28.5
Ingrese escala: C
Resultado: 83.3°F

"""

def conversionAFahrenheit():
    valor = input("ingrese valor Celsius a transformar   ")
    resul = (int(valor) * (9/5)) + 32
    return resul

def conversionACelsius():
    valor = input("ingrese valor Fahrenheit a transformar   ")
    resul = (int(valor) - 32) * (5/9)
    return resul


print("\nEliga una de las opciones \n 1: Celsius a Fahrenheit\n 2: Fahrenheit a Celsius \n")
opcion = int(input("Ingrese la opcion   "))

if opcion == 1:
    print(f"El grado Celsius equivalente en Fahrenheit es: {conversionAFahrenheit()}")
elif opcion == 2:
    print(f"El grado Fahrenheit equivalente en Celsius es: {conversionACelsius()}")
else:
    print("error")

