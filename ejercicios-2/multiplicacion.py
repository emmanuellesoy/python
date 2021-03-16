# Multiplicar sin el signo de multiplicación
def multiplicar(a, b):
    resultado = 0
    for x in range(a):
        resultado += b

    return resultado


print(multiplicar(8, 4))

# Invertir una cadena
nombre = "Emmanuelle"
apellido = "Laguna"
nombreCompleto = nombre + " " + apellido
print(nombreCompleto[::-1])

# Encuentra el número menor de una lista
lista = [1, 2, 5, 3, 55, -24, 13]

menor = "init"

for x in lista:
    if menor == "init":
        menor = x
    else:
        menor = x if x < menor else menor


print(menor)

# Volumen de una esfera


def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3


resultado = calculaVolumen(6)
print(resultado)

# Usuario mayor de edad


def esMayor(usuario):
    return usuario.edad > 17


class Usuario:
    def __init__(self, edad):
        self.edad = edad


usuario = Usuario(15)
usuario2 = Usuario(21)

print(esMayor(usuario))
print(esMayor(usuario2))

# funcion para calcular par o impar


def esPar(x):
    resultado = "Par" if x % 2 == 0 else "Non"
    return resultado


print(esPar(3))
print(esPar(4))


# contar volcales en una palabra
palabra = "MurcielAgo"

vocales = 0
for x in palabra:
    minuscula = x.lower()
    vocales += 1 if minuscula == "a" or minuscula == "e" or minuscula == "i" or minuscula == "o" or minuscula == "u" else 0

print(vocales)


# sumar elementos indefinidos por el usuario

lista = []
print("Ingrese números y para salir escriba \"basta\"")
while True:
    valor = input("Ingrese valor: ")
    if valor == "basta":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("Dato inválido")
            exit()

resultado = 0
for x in lista:
    resultado += x

print(resultado)

# función que reciba nombre y apellido y lo agregue a un archivo


def agregaNombresAArchivo(nombre, apellido):
    archivo = open("nombreCompleto.txt", "a")
    archivo.write(nombre + " " + apellido + "\n")
    archivo.close()


agregaNombresAArchivo("Emmanuelle", "Laguna")
