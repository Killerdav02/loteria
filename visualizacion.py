import matplotlib.pyplot as plt

def graficar_estadisticas(estadisticas):
    aciertos = list(estadisticas.keys())
    frecuencia = list(estadisticas.values())

    plt.bar(aciertos, frecuencia)
    plt.title("Frecuencia de Aciertos en Simulaciones")
    plt.xlabel("Número de Aciertos")
    plt.ylabel("Frecuencia")
    plt.xticks(aciertos)
    plt.grid(True)
    plt.show()
