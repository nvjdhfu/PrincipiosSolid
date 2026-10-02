from abc import ABC, abstractmethod


class Impresora(ABC):

    @abstractmethod
    def imprimir(self):
        pass


class Escaner(ABC):

    @abstractmethod
    def escanear(self):
        pass


class ImpresoraSencilla(Impresora):

    def imprimir(self):
        print("Imprimiendo documento...")


class Multifuncional(Impresora, Escaner):

    def imprimir(self):
        print("Multifuncional imprimiendo...")

    def escanear(self):
        print("Multifuncional escaneando...")


# PRUEBA
impresora = ImpresoraSencilla()
impresora.imprimir()

multifuncional = Multifuncional()
multifuncional.imprimir()
multifuncional.escanear()