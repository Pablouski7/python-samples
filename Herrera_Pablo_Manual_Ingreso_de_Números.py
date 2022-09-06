    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 9/7/2021 
# Objetivo del programa: Calcular la suma, el promedio, el minimo y el máximo de los números que ingrese el usuario.

# Función para recolectar tantos números como indique el usuario. De forma manual
def preguntar_numero(n):
    numeros = []
    for i in range(n):
        nuevo_numero = int(input(f"Factor #{i+1}:"))
        numeros.append(nuevo_numero)
    numeros.sort()
    return numeros
    
# Función para sumar todos los números generados
def sumar(lista):
    acumulador = 0
    for i in range(0,len(lista)):
        acumulador = acumulador + int(lista[i])
    return acumulador

# Obtención, validación de información y declaracion de variables
while True:
    try:
        numero_de_numeros = int(input("Ingresa un número factores que vas a ingresar :"))
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
print("La suma es:",suma)
print("El promedio es:",promedio)
print("El número de menor valor es:",minimo)
print("El número de mayor valor es:",maximo)


    
