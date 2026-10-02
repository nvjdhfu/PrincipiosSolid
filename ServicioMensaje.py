from abc import ABC, abstractmethod


class ServicioMensaje(ABC):

    @abstractmethod
    def enviar(self, mensaje):
        pass


class ServicioSMS(ServicioMensaje):

    def enviar(self, mensaje):
        print(f"SMS enviado: {mensaje}")


class ServicioEmail(ServicioMensaje):

    def enviar(self, mensaje):
        print(f"Email enviado: {mensaje}")


class ServicioWhatsApp(ServicioMensaje):

    def enviar(self, mensaje):
        print(f"WhatsApp enviado: {mensaje}")


class Notificador:

    def __init__(self, servicio):
        self.servicio = servicio

    def enviar_alerta(self, mensaje):
        self.servicio.enviar(mensaje)


# PRUEBA
sms = ServicioSMS()
notificador_sms = Notificador(sms)
notificador_sms.enviar_alerta("Tu pedido está listo.")


email = ServicioEmail()
notificador_email = Notificador(email)
notificador_email.enviar_alerta("Bienvenido al sistema.")


whatsapp = ServicioWhatsApp()
notificador_whatsapp = Notificador(whatsapp)
notificador_whatsapp.enviar_alerta("Tienes una nueva notificación.")