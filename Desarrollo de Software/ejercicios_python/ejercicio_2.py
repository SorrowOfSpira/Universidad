"""
Ejercicio 2
Modifique el programa anterior para que muestre “¡Hola <arg 1>!”. 
Donde arg 1 proviene de la lista de argumentos al ejecutar el programa (ver #53). 
Por ejemplo, al ejecutar: python ejercicio_2.py firulais. 
El programa mostrará “¡Hola Firulais!”. 
Utilice métodos de string para “capitalizar” el argumento recibido por parámetros.
"""
import sys

def main():
    if len(sys.argv) > 1:
            # Mostrar el primer parámetro
            first_param = sys.argv[1]
            first_param = first_param.title()
            print(f"Hola {first_param}")
    else:
            print("No se proporcionaron parámetros.")

if __name__ == "__main__":
    main()