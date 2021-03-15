from camelcase import CamelCase

from index import saludo

saludo("Foo")

c = CamelCase()

s = "esta oración necesita camelcase"

print(s)

print(c.hump(s))
