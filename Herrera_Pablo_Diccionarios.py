    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 10/25/2021 
# Objetivo del programa:
diccionario = {"Primero":"Uno",
               "Segundo":"Dos",
               "Tercero":"Tres",
               "Cuarto":"Cuatro",
               "Quinto":"Cinco",
               "Sexto":"Seis",
               "Septimo":"Siete",
               "Octavo":"Ocho",
               "Noveno":"Nueve",
               "Decimo":"Diez"}
print("->Listar primera vez:")
print(diccionario)
    

print("\n->Borrar 3:")
del(diccionario["Tercero"])
del(diccionario["Sexto"])
del(diccionario["Octavo"])
print(diccionario)

print("\n->Transversar:")
for i,a in diccionario.items():
    print(i,":",a)

print("\n->Insertar 2 valores:")
diccionario["añadido1"] = "Once"
diccionario["añadido2"] = "Doce"

print("->Ordenar por clave:")
print(sorted(diccionario.items()))

