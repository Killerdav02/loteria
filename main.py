import random
import json
import os

boletos_actuales = []


def mostrar_menu():
    print("\n" + "=" * 30)
    print("      LOTERÍA VIRTUAL")
    print("=" * 30)
    print("1. Comprar un boleto manual")
    print("2. Comprar boletos automáticos")
    print("3. Jugar una vez (con boletos actuales)")
    print("4. Ver historial de juegos")
    print("5. Simular múltiples juegos automáticos")
    print("6. Salir")
    print("=" * 30)


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


def generar_numeros_ganadores():
    return sorted(random.sample(range(1, 50), 6))


def jugar_una_vez():
    if not boletos_actuales:
        print("❌ No tienes boletos comprados.")
        return

    ganador = generar_numeros_ganadores()
    print("\n🎯 Números ganadores:", ganador)

    resultados = []
    for boleto in boletos_actuales:
        aciertos = len(set(boleto) & set(ganador))
        premio = calcular_premio(aciertos)
        print(f"Boleto: {boleto} -> Aciertos: {aciertos} → {premio}")
        resultados.append({"boleto": boleto, "aciertos": aciertos, "premio": premio})

    guardar_historial({"ganador": ganador, "resultados": resultados})


def calcular_premio(aciertos):
    premios = {
        3: "Premio pequeño",
        4: "Premio mediano",
        5: "Premio grande",
        6: "🎉 ¡Premio mayor!",
    }
    return premios.get(aciertos, "Sin premio")


def guardar_historial(data, archivo="historial.json"):
    historial = []
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            try:
                historial = json.load(f)
            except json.JSONDecodeError:
                pass

    historial.append(data)

    with open(archivo, "w") as f:
        json.dump(historial, f, indent=4)


def ver_historial(archivo="historial.json"):
    if not os.path.exists(archivo):
        print("No hay historial guardado aún.")
        return

    with open(archivo, "r") as f:
        try:
            historial = json.load(f)
            print("\n📜 HISTORIAL DE JUEGOS:")
            for i, juego in enumerate(historial, 1):
                print(f"\nJuego {i}: Ganador → {juego['ganador']}")
                for r in juego["resultados"]:
                    print(
                        f"  Boleto: {r['boleto']} - Aciertos: {r['aciertos']} - {r['premio']}"
                    )
        except json.JSONDecodeError:
            print("Historial dañado o vacío.")


def simular_juegos():
    try:
        n = int(input("¿Cuántas simulaciones deseas hacer?: "))
        total_aciertos = {i: 0 for i in range(7)}

        for _ in range(n):
            ganador = generar_numeros_ganadores()
            boleto = sorted(random.sample(range(1, 50), 6))
            aciertos = len(set(boleto) & set(ganador))
            total_aciertos[aciertos] += 1

        print("\n Resultados de la simulación:")
        for acierto, cantidad in total_aciertos.items():
            print(f"Aciertos {acierto}: {cantidad} veces")
    except ValueError:
        print("❌ Entrada no válida.")


def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        import os


        if opcion == "1":
            os.system("cls")
            comprar_boleto_manual()
        elif opcion == "2":
            os.system("cls")
            comprar_boletos_automaticos()
        elif opcion == "3":
            os.system("cls")
            jugar_una_vez()
        elif opcion == "4":
            os.system("cls")
            ver_historial()
        elif opcion == "5":
            os.system("cls")
            simular_juegos()
        elif opcion == "6":
            os.system("cls")
            print("👋 ¡Gracias por jugar! Hasta luego.")
            break
        else:
            os.system("cls")
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
