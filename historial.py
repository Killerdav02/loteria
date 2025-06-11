import json
import os

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