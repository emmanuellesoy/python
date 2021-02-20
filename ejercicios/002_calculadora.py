# Ingrese los número a sumar
print("Este programa suma dos números. Ingrese un número o presione t para terminar")
primerNumero = input("Ingrese el primer número ")

if primerNumero == "t" or primerNumero == "T":
    exit()

simbolo = input("Ingrese operación ")

segundoNumero = input("Ingrese el segundo número ")

try:
    primerNumero = int(primerNumero)
    segundoNumero = int(segundoNumero)
    if simbolo == "+":
        print(primerNumero + segundoNumero)
    elif simbolo == "-":
        print(primerNumero - segundoNumero)
    elif simbolo == "*":
        print(primerNumero * segundoNumero)
    elif simbolo == "/":
        print(primerNumero / segundoNumero)
    else:
        print("El simbolo ingresado no es valido")
except:
    print("Alguno de los dos números no es un número")
    exit()
