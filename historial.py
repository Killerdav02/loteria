import json
import os

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
        print("📭 No hay historial disponible.")
        return

    with open(archivo, "r") as f:
        try:
            historial = json.load(f)
        except json.JSONDecodeError:
            print("❌ Error leyendo el historial.")
            return

    print("\n📚 Historial de juegos:")
    for i, juego in enumerate(historial, 1):
        print(f"\nJuego #{i}")
        print("Ganador:", juego["ganador"])
        for resultado in juego["resultados"]:
            print(f"  Boleto: {resultado['boleto']} → Aciertos: {resultado['aciertos']} → {resultado['premio']}")
