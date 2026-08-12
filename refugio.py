import datos, time

def registrar_adoptante():
    adoptantes = []
    adoptante = []
    a = False
    while a == False:
        try:
            nom = input("Ingrese su nombre: ")
            dni = input("Ingrese su DNI: ")
            telefono = input("Ingrese su numero de telefono: ")
            localidad = input("Ingrese su localidad: ")
            if nom.isalpha() and dni.isdigit() and telefono.isdigit() and localidad.isalpha:
                adoptante = ",".join[nom, dni, telefono, localidad]
                adoptantes.append(adoptante)
                return adoptantes, True
            else:
                False
        except Exception:
            False

def agregar_animal():
    ado ptantes = registrar_adoptante()