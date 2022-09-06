    # Datos del estudiante #
# Nombre estudiante: Pablo Herrera
# Código banner: 00326431 
# Fecha: 10/21/2021
# Objetivo del programa: Graficar un diagrama de barras sobre gastos semanales
# o gráficar el radio que hay entre los números de la secuendcia de Fibonacci
import matplotlib.pyplot as plt

# Función para crear el gráfico de barras
def create_bar_chart(data, labels):
    # Número de barras
    num_bars = len(data)
    # Genera los datos de y en función de los datos ingresados para x
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    # Correlaciona las posiciones de y con los datos de x
    plt.yticks(positions, labels)
    plt.xlabel('Monto')
    plt.ylabel('Categorias')
    plt.title('Gastos semanales')
    plt.grid()
    plt.show()

# Función para gráficar
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Número')
    plt.ylabel('Radio')
    plt.title('Radio entre los números consecutivos de Fibonacci')
    plt.show()

# Función para generar la secuencia de Fibonacci y graficar el golden ratio
def fibo():
    # Genera la secuencia de Fibonacci
    serie = [1,1]
    for i in range(10):
        serie.append(serie[-1]+serie[-2])
    # Genera los radios entre los números de la secuencia de Fibonacci
    radios = [1,1]
    for i in range(2,len(serie)):
        radios.append(serie[i]/serie[i-1])
    # Dibuja la gráfica
    draw_graph(serie,radios)
if __name__ == '__main__':
    respuesta = int(input("¿Qué grafico deseas?\n1)Gastos semanales\n2)Golden ratio (Fibonacci)\n:"))
    # Validación del programa a gráficar
    if respuesta == 1:
        # Monto en dolares gastados
        montos = [70,35,30,30]
        # Categorias
        categorias = ['Comida', 'Transporte', 'Entretenimiento','Internet']
        create_bar_chart(montos, categorias)
    elif respuesta == 2:
        fibo()
    else:
        print("Opción no valida")
