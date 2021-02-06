if 2 < 5:
    print("2 es menor que 5")

# a == b
# a < b
# a > b
# a != b
# a <= b
# a => b

if 2 == 2:
    print("2 es igual a 2")

if 2 == 3:
    print("2 es igual a 3")

if 2 > 5:
    print("2 es mayor que 5")

if 2 != 2:
    print("2 es distinto a 2")

if 3 != 2:
    print("3 es distinto a 2")

if 3 <= 3:
    print("3 es menor o igual a 3")

if 3 >= 2:
    print("3 es menor o igual a 2")

if False:
    print("lala")
    print("lala")
    print("lala")
print("lala")

if False:
    print("Solo se imprime si está condición es verdadera")
elif False:
    print("Se imprime si y solo si está condición es verdadera y la anterior fue falsa")
else:
    print("Se imprime si todas de las condiciones anteriores son falsas")

# if en una sola linea
# if 2 < 5: print("2 es menor que 5")

print("Cuando devuelve True") if 5 > 2 else print("Cuando devuelve False")
print("Cuando devuelve True --") if 5 < 2 else print("Cuando devuelve False --")

if 2 < 5 and 3 > 2:
    print("ambas devuelven True")

if 2 < 5 and 3 < 2:
    print("No se puede mostrar si una de las dos condiciones es falsa")

if 1 < 0 or 1 > 0:
    print("Porque una de las dos condiciones es verdadera")

if 1 < 0 or 1 > 2:
    print("No se imprime porque ninguna de las condiciones es verdadera")
