from TDA_Arbol_Binario_RyN_MOD2 import Arbol

#PUNTO 5
def mostrar_dinosaurios_de_x_nombre(arbol, nombre):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            mostrar_dinosaurios_de_x_nombre(arbol.izq, nombre)
        if(arbol.datos['nombre'] == nombre):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            mostrar_dinosaurios_de_x_nombre(arbol.der, nombre)

#PUNTO 7
def mostrar_campo_dinosaurios_de_x_nombre(arbol, nombre, campo):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            mostrar_campo_dinosaurios_de_x_nombre(arbol.izq, nombre, campo)
        if(arbol.datos['nombre'] == nombre):
            print(arbol.info, arbol.datos[campo])
        if(arbol.der is not None):
            mostrar_campo_dinosaurios_de_x_nombre(arbol.der, nombre, campo)

#PUNTO 8
def contar_dinosaurios_de_x_nombre(arbol, nombre):
    contador = 0
    if(arbol.info is not None):
        if(arbol.izq is not None):
            contador += contar_dinosaurios_de_x_nombre(arbol.izq, nombre)
        if(arbol.datos['nombre'] == nombre):
            contador += 1
        if(arbol.der is not None):
            contador += contar_dinosaurios_de_x_nombre(arbol.der, nombre)
    return contador

def ejercicio():
    #PUNTO 1
    dic_dinosaurios = [
        {'nombre' : 'Raptor', 'codigo' : '00001', 'zona' : '1A'},
        {'nombre' : 'Reptil engañoso', 'codigo' : '00002', 'zona' : '2A'},
        {'nombre' : 'Raptor', 'codigo' : '00792', 'zona' : '3A'},
        {'nombre' : 'T-REX', 'codigo' : '00003', 'zona' : '4A'},
        {'nombre' : 'Dientes de dos formas', 'codigo' : '00004', 'zona' : '2B'},
        {'nombre' : 'Sgimoloch', 'codigo' : '00010', 'zona' : '2C'},
        {'nombre' : 'T-REX', 'codigo' : '00005', 'zona' : '3B'},
        {'nombre' : 'T-REX', 'codigo' : '00006', 'zona' : '1P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00006', 'zona' : '2P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00007', 'zona' : '3P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00008', 'zona' : '4P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00009', 'zona' : '1F'},
        {'nombre' : 'Diplodocus', 'codigo' : '00012', 'zona' : '9P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00011', 'zona' : '8P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00013', 'zona' : '7P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00014', 'zona' : '6P'},
        {'nombre' : 'Diplodocus', 'codigo' : '00015', 'zona' : '5P'}
        
        
    ]
    
    arbol_dinosaurio_por_nombre = Arbol()
    arbol_dinosaurio_por_codigo = Arbol()
    
    #PUNTO 2
    arbol_dinosaurio_por_nombre = arbol_dinosaurio_por_nombre.cargar_arbol(dic_dinosaurios, 'nombre')
    arbol_dinosaurio_por_codigo = arbol_dinosaurio_por_codigo.cargar_arbol(dic_dinosaurios, 'codigo')
    
    #PUNTO 3
    print('BARRIDO INORDEN DEL ARBOL DINOSAURIOS ORDENADO POR NOMBRES')
    arbol_dinosaurio_por_nombre.inorden()
    
    #PUNTO 4
    print('\nMOSTRAR TODA LA INFO DEL DINOSAURIO 792')
    print(arbol_dinosaurio_por_codigo.busqueda('00792').datos)
    
    #PUTNO 5
    print('\nMOSTRAR TODA LA INFO DE LOS T-REX')
    mostrar_dinosaurios_de_x_nombre(arbol_dinosaurio_por_nombre, 'T-REX')
    
    #PUNTO 6
    print("\nMODIFICAR EL NOMBRE DE UNA CRIATURA MAL CARGADA")
    info, datos  =  arbol_dinosaurio_por_nombre.eliminar_nodo('Sgimoloch')
    if info is not None:
        info = 'Stygimoloch'
        datos['nombre'] = 'Stygimoloch'
        arbol_dinosaurio_por_codigo.eliminar_nodo(datos['codigo'])
        arbol_dinosaurio_por_codigo = arbol_dinosaurio_por_codigo.insertar_nodo(datos['codigo'], datos)
        arbol_dinosaurio_por_nombre = arbol_dinosaurio_por_nombre.insertar_nodo(info, datos)
    
    #PUNTO 7
    print('\nMOSTRAR LA UBICACION DE TODOS LOS RAPTORES')
    mostrar_campo_dinosaurios_de_x_nombre(arbol_dinosaurio_por_nombre, 'Raptor', 'zona')

    #PUNTO 8
    print('\nCONTAR CUANTOS DIPLODOCUS HAY EN EL GRAFO')
    print('La cantidad de Diplodocus son de: ', contar_dinosaurios_de_x_nombre(arbol_dinosaurio_por_nombre, 'Diplodocus'))
    
    
    
ejercicio()