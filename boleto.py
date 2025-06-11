import random

boletos_actuales = []

def comprar_boleto_manual():
    print("\nIngresa 6 números únicos entre 1 y 49:")
    try:
        numeros = list(map(int, input("Separados por espacios: ").split()))
        if (
            len(numeros) != 6
            or len(set(numeros)) != 6
            or not all(1 <= n <= 49 for n in numeros)
        ):
            raise ValueError
        boletos_actuales.append(sorted(numeros))
        print("✅ Boleto guardado:", sorted(numeros))
    except ValueError:
        print("❌ Entrada no válida. Intenta de nuevo.")


def comprar_boletos_automaticos():
    try:
        cantidad = int(input("¿Cuántos boletos quieres generar?: "))
        for _ in range(cantidad):
            boleto = sorted(random.sample(range(1, 50), 6))
            boletos_actuales.append(boleto)
        print(f"✅ {cantidad} boletos generados automáticamente.")
    except ValueError:
        print("❌ Entrada no válida.")
