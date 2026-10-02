class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido


class GuardadorReporte:
    def guardar(self, reporte, ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(reporte.contenido)

        print("Reporte guardado correctamente.")


# PRUEBA
reporte = Reporte("Este es mi reporte usando el principio SRP.")

guardador = GuardadorReporte()
guardador.guardar(reporte, "reporte.txt")

print("Contenido del reporte:")
print(reporte.contenido)