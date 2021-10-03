from typing import List


class TipoNotificacion:
    def __init__(self, destinatarios=[]):
        self.destinatarios = destinatarios

    def send(self, mensaje: str):
        """
        los métodos abstractos deben generar esta excepción cuando requieren clases derivadas para anular el método.
        """
        raise NotImplementedError


class NotificadorCorreo(TipoNotificacion):
    
    def send(self, mensaje: str):
        print("Enviando a notificador de Email: {}. To: ".format(mensaje), self.destinatarios)


class NotificadorSMS(TipoNotificacion):
    
    def send(self, mensaje: str):
        print("Enviando a notificador de SMS: {} to: ".format(mensaje), self.destinatarios)


class NotificadorFacebook(TipoNotificacion):

    def send(self, mensaje: str):
        print("Enviando a notificador de Facebook: {} to: ".format(mensaje), self.destinatarios)


class NotificadorEmpresa(TipoNotificacion):

    def send(self, mensaje: str):
        print("Enviando a notificador de Empresarial: {} to: ".format(mensaje), self.destinatarios)


class Notificador:
    """""
     1) Correo,
     2) Facebook,
     3) SMS,
     4) Empresa
    """""
    def __init__(self, notificadores={}):
        fabrica = GeneradorNotificadores()
        self.notificadores = fabrica.crearNotificadores(notificadores)

    def send(self, mensaje: str):
        """
         Envia el mensaje a los notificadores existentes en la lista
        """
        for n in self.notificadores:
            n.send(mensaje)


class GeneradorNotificadores:

    def __init__(self):
        """
        # Esta lista contiene todos los TiposNotificador existentes   
        """
        self.notificadoresExistentes = [NotificadorCorreo, NotificadorFacebook, NotificadorSMS, NotificadorEmpresa]

    def crearNotificadores(self, notificadores={}):
        notificadoresCreados = []
        """
        # Se recorren los tipos existentes creando los que sean necesarios según lo indicado en el diccionario
        """
        for key in notificadores.keys():
            destinatarios = notificadores.get(key)
            notificadorNuevo = self.notificadoresExistentes[key](destinatarios)
            notificadoresCreados.append(notificadorNuevo)
        return notificadoresCreados