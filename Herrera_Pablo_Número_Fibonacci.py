    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 10/20/2021
# Objetivo del programa: Dibujar el radio que hay entre los números de la secuendcia de Fibonacci
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Número')
    plt.ylabel('Radio')
    plt.title('Radio entre los números consecutivos de Fibonacci')
    plt.show()

serie = [1,1]
for i in range(10):
    serie.append(serie[-1]+serie[-2])

radios = [1,1]
for i in range(2,len(serie)):
    radios.append(serie[i]/serie[i-1])
    
draw_graph(serie,radios)
