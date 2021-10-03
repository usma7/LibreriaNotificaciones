# LibreriaNotificaciones
Suponga que usted trabaja en una empresa de desarrollo y le asignaron la tarea de modificar una librería de notificación que le permite a otros programas notificar a sus usuarios acerca de eventos importantes.  La versión inicial de la librería estaba basada en la clase Notificador, la cual tiene un método enviar. Este método puede aceptar un mensaje como parámetro de un cliente y enviar el mensaje a una lista de correos que fueron pasados al Notificador vía su constructor. Una aplicación de un tercero, que actúa como cliente, es la que debe crear y configurar el objeto Notificador una vez y luego los usa cada vez que algo importante ocurre. En algún punto, usted se da cuenta que los usuarios de la librería esperan no solo correos de notificación. Muchos de ellos requieren recibir SMS, otros quieren recibir notificaciones vía Facebook y los clientes corporativos quizá quieran recibir notificaciones vía el sistema de mensajería empresarial. Modifique el diseño para esta situación, considerando que pueden ser muchas más opciones de notificación de las mencionadas.  Más adelante algún cliente pregunta: ¿por qué no se pueden usar varios tipos de notificación al mismo tiempo? A usted le piden que modifique nuevamente el diseño para considerar dicha situación, tratando de reutilizar lo que se pueda y dejando el diseño flexible para poder incorporar nuevas opciones.