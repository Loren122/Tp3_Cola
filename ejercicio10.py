from cola import Cola
from pila import Pila
# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:




class Notificacion:

    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje


# Crear la cola de notificaciones
cola_notificaciones = Cola()

def cargar_cola(cola):
     notificaciones = [
        Notificacion("9:30", "Facebook", "Tienes una nueva solicitud de amistad"),
        Notificacion("13:15", "Instagram", "Te han etiquetado en una foto"),
        Notificacion("11:00", "Twitter", "Nuevo retweet en tu publicación sobre Python"),
        Notificacion("15:45", "Twitter", " ¡Noticia destacada de Python!")
     ]
     # Agregar notificaciones a la cola
     for notificacion in notificaciones:
         cola.arrive(notificacion)
         

# Mostrar las notificaciones de la cola
# while cola_notificaciones.size() > 0:
#     notificacion = cola_notificaciones.atention()
#     print(f"Hora: {notificacion.hora}")
#     print(f"Aplicación: {notificacion.aplicacion}")
#     print(f"Mensaje: {notificacion.mensaje}")


# a. escribir una función que elimine de la cola todas las notificaciones de Facebook
def borrar_notif_facebook(cola):

    for i in range(cola.size()):
        if cola.on_front().aplicacion == "Facebook":
            cola.atention()


# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, sin perder datos en la cola
def twitter_python(cola):
    notif_verificadas = 0

    while notif_verificadas < cola.size():
        notificacion = cola.atention()
        if notificacion.aplicacion == "Twitter":
            if "Python" in notificacion.mensaje:

                print(f"Hora: {notificacion.hora}")
                print(f"Aplicación: {notificacion.aplicacion}")
                print(f"Mensaje: {notificacion.mensaje}")
                print()

        cola.arrive(notificacion)
        notif_verificadas += 1


# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.
def almacenar_notif(cola):
    pila_temp = Pila()
    contador = 0

    for i in range(cola.size()):
        notificacion = cola.move_to_end()
        hora = notificacion.hora

        if "11:43" <= hora <= "15:57":
            contador += 1
            pila_temp.push(notificacion)

    return contador, pila_temp


cola_notificaciones = Cola()
cargar_cola(cola_notificaciones)
borrar_notif_facebook(cola_notificaciones)

print('---------------------------------------------')

print('Notificaciones de Facebook borradas:'), print()
while cola_notificaciones.size() > 0:
    notificacion = cola_notificaciones.atention()
    print(f"Hora: {notificacion.hora}")
    print(f"Aplicación: {notificacion.aplicacion}")
    print(f"Mensaje: {notificacion.mensaje}"), print()
    
print('---------------------------------------------')

cargar_cola(cola_notificaciones)
print("Notif. de Twitter cuyo mensaje incluye 'Python':"), print()
twitter_python(cola_notificaciones)

print('---------------------------------------------')

cont, pila = almacenar_notif(cola_notificaciones)

print(f'Cantidad de notificaciones entre las 11:43 y las 15:57: [{cont}]'), print()

print('Notificaciones entre ese horario:'), print()
while pila.size() > 0:
    notificacion = pila.pop()
    print(f"Hora: {notificacion.hora}")
    print(f"Aplicación: {notificacion.aplicacion}")
    print(f"Mensaje: {notificacion.mensaje}"), print()
