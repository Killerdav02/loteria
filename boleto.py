import random

def generar_boleto_manual(numeros):
    if len(set(numeros)) != len(numeros):
        raise ValueError("Los números deben ser únicos.")
    if not all(1 <= n <= 49 for n in numeros):
        raise ValueError("Los números deben estar entre 1 y 49.")
    return sorted(numeros)

def generar_boleto_aleatorio(cantidad=6):
    return sorted(random.sample(range(1, 50), cantidad))
