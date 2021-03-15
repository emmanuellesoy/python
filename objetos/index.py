import "../funciones/funciones"


class Usuario:
    def __init__(self, nombre="", apellido=""):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)


usuario = Usuario("Emmanuelle", "Laguna")
print(usuario.nombre, usuario.apellido)

usuario2 = Usuario("Juan", "Perez")
print(usuario2.nombre, usuario2.apellido)

usuario3 = Usuario()
print(usuario3.nombre, usuario3.apellido)

usuario.saludar()
usuario2.saludar()
usuario3.saludar()


class Administrador(Usuario):
    def superSaludo(self):
        print("Hola!, mi nombre es", self.nombre,
              self.apellido, "y soy un administrador")


administrador = Administrador("Pepe", "Pecas")
administrador.superSaludo()
administrador.saludar()


class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludar(self):
        print("Hola, soy un", self.tipo, "y mi sonido es el", self.onomatopeya)


class Gato(Animal):
    tipo = "gato"

    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        # Animal.__init__(self, nombre, onomatopeya)


class Perro(Animal):
    tipo = "perro"


class Canario(Animal):
    tipo = "canario"


gato = Gato("Foo", "maullido")
perro = Perro("Molly", "ladrido")
canario = Canario("Piolin", "trino")

gato.saludar()
perro.saludar()
canario.saludar()
