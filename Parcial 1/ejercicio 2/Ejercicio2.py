from tdaPila import Pila
from tdaCola import Cola


def eliminarNotisFacebook(objCola):
    eliminado = 0;
    largo = objCola.tamanio()

    for i in range(0, largo):

        if objCola.en_frente()[1] == 'Facebook':
            objCola.atencion()
            largo = largo - 1
        else:
            objCola.mover_final()

def mostrarMensajesTwitterQueContenganMnesajePython(objCola):
    estPython = False

    for i in range(0,objCola.tamanio()):
        vector = objCola.en_frente()

        if (vector[2].find('Python') != -1) and (vector[1] == 'Twitter'):
            print(objCola.en_frente())
        
        objCola.mover_final()

def mostrarNotisInstagram(objCola):
    objPila = Pila()

    for i in range(0,objCola.tamanio()):

        if (objCola.en_frente()[1] == 'Instagram'):
            objPila.apilar(objCola.en_frente())

        objCola.mover_final()
        
    while(not objPila.pila_vacia()):
        print(objPila.desapilar())



def ejercicio2():
    objCola = Cola()

    lsitaNotificaciones = [
                            ['', 'Facebook', ''],
                            ['', 'Twitter', ''],
                            ['', 'Twitter', 'hola gente esto Python debe contener'],
                            ['', 'Facebook', ''],
                            ['', 'Instagram', 'hola gente esto Python debe contener'],
                            ['', 'Facebook', ''],
                            ['', 'Twitter', 'hola gente esto Python debe contener'],
                            ['', 'Instagram', ''],
                            ]

    for lista in lsitaNotificaciones:
        objCola.arribo(lista)
        
    eliminarNotisFacebook(objCola)

    mostrarMensajesTwitterQueContenganMnesajePython(objCola)
    print('')
    mostrarNotisInstagram(objCola)

ejercicio2()

