def miFuncion():
    print("Mi primera función")


miFuncion()


def imprimirDato(dato):
    print(dato)


imprimirDato("a")


def imprimirDatos(*datos):
    print(datos)


imprimirDatos("Uno", "Dos", "Tres")


def nombreCompleto(apellido, nombre):
    print(nombre, apellido)


nombreCompleto(nombre="Emmanuelle", apellido="Laguna")


def imprmirNombreCompleto(**nombreCompleto):
    print(nombreCompleto["nombre"], nombreCompleto["apellido"])


imprmirNombreCompleto(nombre="Emmanuelle", apellido="Laguna")


def imprmirArgumento(argumento="Sin datos de entrada"):
    print(argumento)


imprmirArgumento()
imprmirArgumento("Con datos de entrada")
