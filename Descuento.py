class Descuento:
    def aplicar(self, precio):
        return precio


class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.80


class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.90


class DescuentoCorporativo(Descuento):
    def aplicar(self, precio):
        return precio * 0.85


# PRUEBA
precio = 100

vip = DescuentoVIP()
estudiante = DescuentoEstudiante()
corporativo = DescuentoCorporativo()

print("Precio original:", precio)
print("Precio VIP:", vip.aplicar(precio))
print("Precio estudiante:", estudiante.aplicar(precio))
print("Precio corporativo:", corporativo.aplicar(precio))