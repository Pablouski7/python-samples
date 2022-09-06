    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 9/21/2021 
# Objetivo del programa: Calcular la suma, el promedio, el minimo y el máximo a partir de datos generados aleatoriamente.

# Import para recibir funciones de aleatoriedad
import random

# Ciclo para ejecutar el programa hasta obtener datos validos
while True:
    try:
        # Obtención del número de datos a generar
        numero_de_numeros = int(input("Ingresa el número que desees : "))    
        # Condicional que valida que el número sea positivo
        if numero_de_numeros <= 0:
            print("Ingrese un número valido")
        else:
            # Variables necesarias para el lazo for y los calculos a realizar
            minimo = 0
            maximo = 0
            suma = 0

            # Lazo for que genera números aleatorios, hace la suma total, determina el mínimo y máximo a partir del número ingresado
            for i in range(numero_de_numeros):
                # Generador de números aleatorios entre 1 y el triple del número ingresado más 5
                nuevo_numero = random.randint(1,(numero_de_numeros*3)+5)
                print(nuevo_numero)
                if i == 0:
                    minimo = nuevo_numero
                    maximo = nuevo_numero
                suma = suma + nuevo_numero
                if minimo > nuevo_numero:
                    minimo = nuevo_numero
                if maximo < nuevo_numero:
                    maximo = nuevo_numero
                
            promedio = round(suma/numero_de_numeros,2)

            # Exposición de datos
            print("El número ingresado fue:",numero_de_numeros)
            print("La suma total es:",suma)
            print("El promedio es:",promedio)
            print("El número de menor valor es:",minimo)
            print("El número de mayor valor es:",maximo)
            break
    except (RuntimeError, TypeError, NameError, ValueError, ZeroDivisionError):
        print("Ingrese un número valido")


    
