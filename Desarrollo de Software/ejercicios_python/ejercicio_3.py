"""
Ejercicio 3
Escriba un programa con las funciones necesarias para realizar 
las operaciones de: suma, resta, multiplicación y división. 
El programa deberá llevar a cabo todas las operaciones al recibir dos parámetros numéricos 
durante la ejecución del mismo. Ver input().

Ejemplo:
Operación suma
Ingrese operador 1: 1
Ingrese operador 2: 2
Resultado: 3
"""

def suma (a,b):
    global condicion
    condicion = 0
    resul = a + b
    return resul

def resta(a,b):
    global condicion
    condicion = 0
    resul = a - b
    return resul

def division(a,b):
    global condicion
    condicion = 0
    resul = a / b
    return float(resul)

def multiplicacion(a,b):
    global condicion
    condicion = 0
    resul = a * b
    return resul


print("Elija una de las siguientes opciones para hacer una operacion matematica\n 1: Suma \n 2: Resta\n 3: Division\n 4: Multiplicacion\n")
eleccion = int(input("Ingrese su eleccion:"))
op1 = int(input("ingrese operador 1: "))
op2 = int(input("ingrese operador 2: "))

condicion = 1
print("El resultado es: ")
while (condicion):
    if eleccion == 1:
        print(suma(op1,op2))
    elif eleccion == 2:
        print(resta(op1,op2))
    elif eleccion == 3:
        print(division(op1,op2))
    elif eleccion == 4:
        print(multiplicacion(op1,op2))
    else:
        print("Operacion invalida")
        break
