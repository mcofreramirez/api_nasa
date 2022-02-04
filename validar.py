


def validate(opciones, eleccion):
    while eleccion not in opciones:
        eleccion = input("Ha ingresado una opcion no valida, por favor escoja algunas de las opciones disponibles:")

    return eleccion

if __name__ == '__main__':
    opciones = ['1','2','3']
    eleccion = input("Escoja una opcion:")
    validate(opciones,eleccion)
