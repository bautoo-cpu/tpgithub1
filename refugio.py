import time, datos

def registrar_adoptante():
    adoptante = []
    while False:
        try:
            nom = input("ingrese su nombre: ")
            if nom.isalpha():
                nom.list()
                dni = int(input("ingrese su DNI: "))
                telephone = int (input("ingrese su numero de telefono: "))
                localidad = int(input("ingrese su localidad: "))
        except Exception:
            False

def agregar_animal():
