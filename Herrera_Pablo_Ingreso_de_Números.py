    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 9/7/2021 
# Objetivo del programa: Calcular la suma, el promedio, el minimo y el máximo de ya sea una lista autogenerada o de los datos que ingrese el usuario.

# Función para recolectar tantos números como indique el usuario. De forma manual
def preguntar_numero(n):
    numeros = []
    for i in range(n):
        nuevo_numero = int(input(f"Factor #{i+1}:"))
        numeros.append(nuevo_numero)
        numeros.sort()
    return numeros

# Función para generar una lista de números aleatorios en base al dato ingresado por el usuario
import random

def agregar_n_numeros(n):
    numeros = []
    for i in range(n+1):
        numero = random.randint(1,n)
        numeros.append(numero)
        numeros.sort()
    return numeros
        
# Función para sumar todos los números de una lista
def sumar(lista):
    acumulador = 0
    for i in range(0,len(lista)):
        acumulador = acumulador + int(lista[i])
    return acumulador

# Ciclo para ejecutar el programa hasta recibir los datos apropiados
while True:
    try:
        # Elección de programa
        print("1. Quiero ingresar de forma manual los datos")
        print("2. Quiero que se autogeneren los datos conrespecto al número que yo ingrese")
        programa_elegido = int(input("Eliga la opción 1 o 2: "))

        # Condicional que ejecuta uno de los dos programas
        if(programa_elegido == 1):

            # Obtención, validación de información y declaracion de variables
            while True:
                try:
                    numero_de_numeros = int(input("Ingresa el número factores que vas a ingresar :"))
                    lista_de_numeros = preguntar_numero(numero_de_numeros)
                    suma = sumar(lista_de_numeros)
                    promedio = round(suma/len(lista_de_numeros))
                    maximo = lista_de_numeros[len(lista_de_numeros)-1]
                    minimo = lista_de_numeros[0]
                    break
                except (RuntimeError, TypeError, NameError, ValueError, ZeroDivisionError):
                    print("Oops!  Eso no era un número entero positivo. Intenta de nuevo")

            # Exposición de datos
            print("Número ingresado:",numero_de_numeros)
            print("Lista generada:",lista_de_numeros)
            print("La suma total es:",suma)
            print("El promedio es:",promedio)
            print("El número de menor valor es:",minimo)
            print("El número de mayor valor es:",maximo)
            
        elif(programa_elegido == 2):

            # Obtención, validación de información y declaracion de variables
            while True:
                try:
                    numero_de_numeros = int(input("Ingresa un número entero positivo: "))
                    lista_de_numeros = agregar_n_numeros(numero_de_numeros)
                    suma = sumar(lista_de_numeros)
                    promedio = round(suma/len(lista_de_numeros))
                    maximo = lista_de_numeros[len(lista_de_numeros)-1]
                    minimo = lista_de_numeros[0]
                    break
                except (RuntimeError, TypeError, NameError, ValueError, ZeroDivisionError):
                    print("Oops!  Eso no era un número entero positivo. Intenta de nuevo")

            # Exposición de datos
            print("Número ingresado:",numero_de_numeros)
            print("Lista generada:",lista_de_numeros)
            print("La suma total es:",suma)
            print("El promedio es:",promedio)
            print("El número de menor valor es:",minimo)
            print("El número de mayor valor es:",maximo)
        else:
            print("Ingrese una opción valida")
        break
    except (RuntimeError, TypeError, NameError, ValueError, ZeroDivisionError):
        print("Ingrese una opción valida")




    
