# Funciones para evitar el ingreso de datos no validos
def validar_positivos(number):
    if number > 0:
        return float(number)
    else:
        print("Ingresa un sueldo valido")
def validar_numero_de_cedula(cedula):
    if cedula.isnumeric():
        numero_de_digitos = 0
        for caracter in cedula:
            numero_de_digitos+= 1
        if numero_de_digitos == 10:
            return cedula
        else:
            print("Ingrese un número de cedula valido")
    else:
        print("Ingrese un número de cedula valido")

# Obtención de datos
nombre = input("Cuál es tu nombre: ")
apellido = input("Cuál es tu apellido: ")
cedula = validar_numero_de_cedula(input("Cuál es tu cedula: "))
sueldo = validar_positivos(int(input("Cuál es tu sueldo: ")))
aporte_IESS = round((sueldo * 9.45)/100,2)
sueldo_liquido = round(sueldo - aporte_IESS,2)

# Exposición de datos
print("")
print("El ciudadano que utilizó este programa")
print("Tiene de nombre ",nombre," y apellido ",apellido)
print("Con número de cedula: ", cedula)
print("Actualmente recibe un sueldo bruto de: $",sueldo)
print("Aportando así al IESS un total de: $",aporte_IESS)
print("Siendo entonces su sueldo liquido de: $",sueldo_liquido)

# Datos del estudiante
print("")
print("Nombre estudiante: Pablo Herrera")
print("Código banner: 00326431")
print("Fecha: 9/29/2021")
print("Objetivo del programa: Solicitar datos generales al usuario, para calcular su aporte al IESS")
