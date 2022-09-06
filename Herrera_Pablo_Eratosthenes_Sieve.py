  # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 10/5/2021
# Objetivo del programa: Cálcular todos los números primos inferiores al número ingresado

# Declaración de variables
n = int(input("Ingrese un número: "))
primes = []
isPrime = [1 for i in range(n)]
isPrime[0] = isPrime[1] = 0
# Lazo for para ejecutar por cada número menor del n ingresado
for i in range(n):
        # Comprobación de si i es un número primo o no
	if isPrime[i]:
		primes.append(i)
		h = 2
		while i*h < n:
			isPrime[i*h] = 0
			h += 1
# Exposición de datos
print("Los números primos dentro de",n,"son :",primes)
