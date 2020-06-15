#simple print
print("hola mundo estructural")


#print en programacion orientada a objetos
class saludo:
    def __init__(self, texto):
        self.texto= texto

objsaludo = saludo("Hola mundo en poo")
print(objsaludo.texto)
