datos = open("datos.txt", "a")

datos.write(
    "Se agrega justo al termino del archivo, sin espacio o saltos de linea")
datos.write("\nagregando una nueva linea desde python")
datos.write("\nagregado segunda linea")

datos.close()
