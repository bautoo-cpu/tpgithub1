import os, refugio, datos, time

def main():
    opcion = ""
    menu = ["¡Bienvenido al refugio Huellas!", "1. Agregar animal", "2. Adoptar animal", "3. Reservar animal", "4. Salir"]
    while opcion != "5":
        os.system("cls")
        for e in menu:
            print(e)
            time.sleep(0.1)
        opcion = input("Elija una opcion: ")
        if opcion == "1":
            refugio.agregar_animal()
        elif opcion == "2":
            refugio.adoptar_animal()
        elif opcion == "3":
            refugio.reservar_animal()
        elif opcion == "4":
            print("Programa finalizado.")
            time.sleep(1)
        else:
            print("Opcion invalida")
            time.sleep(1)
main()