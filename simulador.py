import random
from loteria import generar_numeros_ganadores

def simular_juegos():
    try:
        n = int(input("¿Cuántas simulaciones deseas hacer?: "))
        total_aciertos = {i: 0 for i in range(7)}

        for _ in range(n):
            ganador = generar_numeros_ganadores()
            boleto = sorted(random.sample(range(1, 50), 6))
            aciertos = len(set(boleto) & set(ganador))
            total_aciertos[aciertos] += 1

        print("\nResultados de la simulación:")
        for acierto, cantidad in total_aciertos.items():
            print(f"Aciertos {acierto}: {cantidad} veces")
    except ValueError:
        print("❌ Entrada no válida.")
