from libreria_notificadores import Notificador


# Opciones del menú en consola, asociamos un numero a cada tipo de notificador
MenuConsola = {
    1: "Correo",
    2: "Facebook",
    3: "SMS",
    4: "Empresarial",
}

# Muestra los tipos de notificador existentes
print("""
1. Correo
2. Facebook
3. SMS
4. Empresarial

""")

tipoNotificador = input("Elija el tipo de notificador.\nEscriba todos los números seleccionados sin ninguna separación:\n")
datosNotificador = {}

for n in tipoNotificador:
    """
    Recorre todos los notificadores seleccionados, luego agrega los destinatarios al notificador
    """
    destinatarios = input("Elija los destinatarios para el notificador de {} separados por una coma: ".format(MenuConsola.get(int(n))))
    destinatarios = destinatarios.split(',') # Convierte los destinatarios a una lista
    datosNotificador.update({int(n) - 1: destinatarios})

notificador = Notificador(datosNotificador)
mensajeEnviar = input("Mensaje a enviar: ")

# Envía el mensaje al notificador
notificador.send(mensajeEnviar)