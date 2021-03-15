import os

if os.path.exists("datos.txt"):
    os.remove("datos.txt")
else:
    print("El archivo no existé")
