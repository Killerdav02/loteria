import random

def generar_numeros_ganadores(cantidad=6):
    return sorted(random.sample(range(1, 50), cantidad))

def comparar_boletos_con_ganador(boletos, ganador):
    resultados = []
    for boleto in boletos:
        aciertos = len(set(boleto) & set(ganador))
        resultados.append((boleto, aciertos, calcular_premio(aciertos)))
    return resultados

def calcular_premio(aciertos):
    premios = {
        3: "Premio pequeño",
        4: "Premio mediano",
        5: "Premio grande",
        6: "¡Premio mayor!"
    }
    return premios.get(aciertos, "Sin premio")
