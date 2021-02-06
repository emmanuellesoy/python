# Ingrese los número a sumar
print("Este programa suma dos números. Ingrese un número o presione t para terminar")
primerNumero = input("Ingrese el primer número ")

if primerNumero == "t" or primerNumero == "T":
    exit()

segundoNumero = input("Ingrese el segundo número ")

try:
    primerNumero = int(primerNumero)
    segundoNumero = int(segundoNumero)
    print(primerNumero + segundoNumero)
except:
    print("Alguno de los dos números no es un número")
