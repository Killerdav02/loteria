from historial import ver_historial
from simulador import simular_juegos
from boleto import comprar_boleto_manual, comprar_boletos_automaticos
from loteria import jugar_una_vez



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
