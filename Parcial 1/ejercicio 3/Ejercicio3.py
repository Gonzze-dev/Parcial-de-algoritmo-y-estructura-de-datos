from tdaLista import Lista

def getPosThor(objLista):
    for i in range(0, objLista.tamanio()):

        if objLista.obtener_elemento(i)['name'] == "Thor":
            return i
    
    return None

def mostrarPosThor(numero):
    if numero is not None:
        numero = numero -1
        print('Thor esta en la posicion: ', numero)
    else:
        print('Thor no esta en la lista')

        
    
def modificarNombreScarlet(objLista):
    for i in range(0, objLista.tamanio()):
        elemento = objLista.obtener_elemento(i)

        if(elemento['name'] == "Scalet Witch"):
            elemento['name'] = "Scarlet Witch"
            objLista.modificar_elemento(i, elemento, 'name')


def agregarPersonajesDeOtraLista(objListaRecibe, objListaDa):
    conjunto = []

    for i in range(0, objListaRecibe.tamanio()):
        conjunto.append(objListaRecibe.obtener_elemento(i))

    for i in range(0, objListaDa.tamanio()):

        if objListaDa.obtener_elemento(i) not in conjunto:
            objListaRecibe.insertar(objListaDa.obtener_elemento(i), 'name')

def barridoDesendente(objLista):
    for i in range(0, objLista.tamanio()):
        print(objLista.obtener_elemento(objLista.tamanio()-1-i))

def mostrarPersonajeDeLaPosicionSiete(objLista):

    if objLista.tamanio() >= 7:
        print(objLista(6))

def mostrarPersonajesConCoS(objLista):

    for i in range(0, objLista.tamanio()):
        if objLista.obtener_elemento(i)['name'][0] in ['C','S']:
            print(objLista.obtener_elemento(i))

def ejercicio3():
    objLista = Lista()
    objLista2 = Lista()
    criterio = 'name'
    Pos = None

    personajesMarvel = [
                        {'name' : 'Thor', 'anio' : 1992, 'Heroe' : True},
                        {'name' : 'Scalet Witch', 'anio' : 2000, 'Heroe' : False},
                        {'name' : 'Scalet Witch', 'anio' : 1965, 'Heroe' : False},
                        ]
    
    personajesMarvel2 = [
                        {'name' : 'Black Widow', 'anio' : 2006, 'Heroe' : True},
                        {'name' : 'Hulk', 'anio' : 2006, 'Heroe' : False},
                        {'name' : 'Rcoket Racoonn','anio' : 2020, 'Heroe' : False},
                        {'name' : 'Loki', 'anio' : 1950, 'Heroe' : True},
                        ]   

    for personaje in personajesMarvel:
        objLista.insertar(personaje, criterio)
    
    for personaje in personajesMarvel2:
        objLista2.insertar(personaje, criterio)

    mostrarPosThor(getPosThor(objLista))
    modificarNombreScarlet(objLista)
    agregarPersonajesDeOtraLista(objLista, objLista2)


    #asendente
    objLista.barrido()
    print('')
    barridoDesendente(objLista)

    print('')

    mostrarPersonajesConCoS(objLista)

    print('Barrido por nombre')
    if criterio != 'name':
        objLista.ordenar('name')
        
    objLista.barrido()
    print('\nBarrido por año')
    objLista.ordenar('anio')
    objLista.barrido()



ejercicio3()