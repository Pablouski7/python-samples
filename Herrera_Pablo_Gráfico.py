    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 10/14/2021
# Objetivo del programa: Graficar la función trigonométrica de Seno.
import matplotlib.pyplot as plt
import math

# Función para dibujar una gráfica
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.title('Función Seno')
    plt.show()

def generate_x_y():
    # genera valores para x
    x_values = range(-1000,1001,50)
    # lista vacia para almacenar valores de y
    y_values = []
    # aplicar la función seno a todas las x's para conseguir las y's
    for i in x_values:
        y_values.append(math.sin(i))
    # llamar a la función para gráficar
    draw_graph(x_values,y_values)

# Ejecución del programa
if __name__=='__main__':
    generate_x_y()
