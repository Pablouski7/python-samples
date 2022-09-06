    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 10/7/2021
# Objetivo del programa: Determinar si el número ingresado es un primo o no.

# Obtención de datos
numero_ingresado = int(input("Ingrese un número: "))

# Divisores de todo número primo
divisores = {1,numero_ingresado}

# Ciclo for para hallar los submultiplos del número ingresado
for i in range(2,int(numero_ingresado**0.5)):
    if numero_ingresado%i==0:
        divisores.add(i)
        break

# Validación del número de divisores que tiene el número ingresado. Y por ende de si es primo o no.
if (len(divisores) > 2):
    print(numero_ingresado,"no es primo")
else:
    print(numero_ingresado,"es primo")
