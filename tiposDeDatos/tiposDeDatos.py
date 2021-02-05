# strings
palabra = 'hola mundo'
oracion = "hola mundo con comilla doble"

# numericos
entero = 20
flotante = 20.2
complejos = 1j

# print(palabra, oracion, entero, flotante, complejos)

lista = [1, 2, 3]
print(lista)

lista.append(4)

lista2 = lista.copy()

print(lista)

lista.clear()
print(lista)

print(lista2)

print("Cuenta cuantos 1 hay en lista2: ", lista2.count(1))

print("Longitud de lista2: ", len(lista2))

print("El segundo elemento de lista2 es \"lista[1]\": ", lista2[1])

lista2 = ["Hola", "Hola", "Mundo Feliz", "Chanchito Feliz", "Otra oración"]

lista2.pop()  # Elimina el último elemento de la lista
print(lista2)

lista2.append(4)

lista2.remove("Hola")  # Elimina la primer coincidencia
print(lista2)

lista2.reverse()
print(lista2)

lista2[0] = "Chanchito Triste"
print(lista2)

lista2.sort()
print(lista2)


# Tuplas
tupla = ('hola', 'mundo', 'somos', 'tupla')
print(tupla)
print(tupla.index("somos"))
print(tupla[2])

listaDeTupla = list(tupla)
print(listaDeTupla)

# rangos

rango = range(6)
print(rango)
