class Ave:
    def mover(self):
        return "El ave se está moviendo"


class AveVoladora(Ave):
    def mover(self):
        return "El ave está volando"

    def volar(self):
        return "Volando..."


class Pinguino(Ave):
    def mover(self):
        return "El pingüino está nadando"

    def nadar(self):
        return "Nadando..."


def mostrar_movimiento(ave):
    print(ave.mover())


# PRUEBA
ave_voladora = AveVoladora()
pinguino = Pinguino()

mostrar_movimiento(ave_voladora)
mostrar_movimiento(pinguino)

print(ave_voladora.volar())
print(pinguino.nadar())