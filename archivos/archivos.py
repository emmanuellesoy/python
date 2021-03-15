datos = open("datos.txt")
# print(datos.read())

# print(datos.readline())
# print(datos.readline())
# print(datos.readline())
# print(datos.readline())
# print(datos.readline())


for dato in datos:
    print(dato)

datos.close()
