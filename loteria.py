import random
from historial import guardar_historial
from boleto import boletos_actuales

def generar_numeros_ganadores():
    return sorted(random.sample(range(1, 50), 6))

def calcular_premio(aciertos):
    premios = {
        3: "Premio pequeño",
        4: "Premio mediano",
        5: "Premio grande",
        6: "🎉 ¡Premio mayor!",
    }
    return premios.get(aciertos, "Sin premio")

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
