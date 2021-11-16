from grafos import Grafo

#PUNTO 1
def insertar_vertices_en_grafo(grafo):
    grafo.insertar_vertice('Manjaro', {'tipo' : 'PC'})
    grafo.insertar_vertice('Parrot', {'tipo' : 'PC'})
    grafo.insertar_vertice('Fedora', {'tipo' : 'PC'})
    grafo.insertar_vertice('Mint', {'tipo' : 'PC'})
    grafo.insertar_vertice('Ubuntu', {'tipo' : 'PC'})
    
    grafo.insertar_vertice('Red Hat', {'tipo' : 'Notebook'})
    grafo.insertar_vertice('Debian', {'tipo' : 'Notebook'})
    grafo.insertar_vertice('Arch', {'tipo' : 'Notebook'})
    
    grafo.insertar_vertice('Impresora', {'tipo' : 'Impresora'})
    
    grafo.insertar_vertice('Guarani', {'tipo' : 'Servidor'})
    grafo.insertar_vertice('MongoDB', {'tipo' : 'Servidor'})
    
    grafo.insertar_vertice('Switch 1', {'tipo' : 'Switch'})
    grafo.insertar_vertice('Switch 2', {'tipo' : 'Switch'})
    
    grafo.insertar_vertice('Router 1', {'tipo' : 'Router'})
    grafo.insertar_vertice('Router 2', {'tipo' : 'Router'})
    grafo.insertar_vertice('Router 3', {'tipo' : 'Router'})

def insertar_aristar_en_grafo(grafo : Grafo):
    grafo.insertar_arista(40, 'Manjaro', 'Switch 2')
    grafo.insertar_arista(12, 'Parrot', 'Switch 2')
    grafo.insertar_arista(5, 'MongoDB', 'Switch 2')
    grafo.insertar_arista(56, 'Arch', 'Switch 2')
    grafo.insertar_arista(40, 'Fedora', 'Switch 2')
    
    grafo.insertar_arista(61, 'Switch 2', 'Router 3')
    
    grafo.insertar_arista(17, 'Debian', 'Switch 1')
    grafo.insertar_arista(18, 'Ubuntu', 'Switch 1')
    grafo.insertar_arista(22, 'Impresora', 'Switch 1')
    grafo.insertar_arista(80, 'Mint', 'Switch 1')
    
    grafo.insertar_arista(29, 'Switch 1', 'Router 1')
    
    grafo.insertar_arista(37, 'Router 1', 'Router 2')
    grafo.insertar_arista(43, 'Router 1', 'Router 3')
    
    grafo.insertar_arista(50, 'Router 3', 'Router 2')
    
    grafo.insertar_arista(25, 'Red Hat', 'Router 2')
    grafo.insertar_arista(9, 'Guarani', 'Router 2')

#PUNTO 2
def deshacer_visitado(grafo, ver_origen = 0):
    while(ver_origen < grafo.inicio.tamanio()):
        vertice = grafo.inicio.obtener_elemento(ver_origen)
        if(vertice['visitado']):
            vertice['visitado'] = False
            aristas = 0
            while(aristas < vertice['aristas'].tamanio()):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = grafo.buscar_vertice(arista['destino'])
                nuevo_vertice = grafo.inicio.obtener_elemento(pos_vertice)
                if(nuevo_vertice['visitado']):
                    deshacer_visitado(grafo, pos_vertice)
                aristas += 1
        ver_origen += 1


def barrido_en_profundidad_desde_x_vertice(grafo : Grafo, nombre):
    pos = grafo.buscar_vertice(nombre)
    
    if(pos != -1):
        grafo.barrido_profundidad(pos)
        deshacer_visitado(grafo)
    else:
        print('El vertice "', nombre, '" no existe')

def barrido_en_amplitud_desde_x_vertice(grafo : Grafo, nombre):
    pos = grafo.buscar_vertice(nombre)
    
    if(pos != -1):
        grafo.barrido_amplitud(pos)
        deshacer_visitado(grafo, pos)
    else:
        print('El vertice "', nombre, '" no existe')

#PUNTO 3
def hallar_camino_mas_corto(grafo, origen, destino):
    vertice_origen = grafo.buscar_vertice(origen)
    vertice_destino = grafo.buscar_vertice(destino)
    costo = None
    
    if vertice_origen != -1 and vertice_destino != -1:
        camino = grafo.dijkstra(vertice_origen)
        while(not camino.pila_vacia()):
            dato = camino.desapilar()
            if(dato[1][0] == destino):
                if(costo is None):
                    costo = dato[0]
                print('paso por: ', dato[1][0])
                destino = dato[1][1]
        print('el costo total del camino es: ', costo)


def ejercicio():
    grafo = Grafo(dirigido=False)
    
    #PUTNO 1
    insertar_vertices_en_grafo(grafo)
    insertar_aristar_en_grafo(grafo)
    
    #PUNTO 2
    print('\nBARRIDO EN PROFUNDIDAD DE Red Hat')
    barrido_en_profundidad_desde_x_vertice(grafo, 'Red Hat')
    
    print('\nBARRIDO EN AMPLITUD DE Red Hat')
    barrido_en_amplitud_desde_x_vertice(grafo, 'Red Hat')

    print('\nBARRIDO EN PROFUNDIDAD DE Debian')
    barrido_en_profundidad_desde_x_vertice(grafo, 'Debian')
    
    print('\nBARRIDO EN AMPLITUD DE Debian')
    barrido_en_amplitud_desde_x_vertice(grafo, 'Debian')
    
    print('\nBARRIDO EN PROFUNDIDAD DE Arch')
    barrido_en_profundidad_desde_x_vertice(grafo, 'Arch')
    
    print('\nBARRIDO EN AMPLITUD DE Arch')
    barrido_en_amplitud_desde_x_vertice(grafo, 'Arch')
    
    #PUNTO 3
    print('\nENCONTRAR EL CAMINO MAS CORTO DE Debian a MongoDB')
    hallar_camino_mas_corto(grafo, 'Debian', 'MongoDB')
    
    print('\nENCONTRAR EL CAMINO MAS CORTO DE Red Hat a MongoDB')
    hallar_camino_mas_corto(grafo, 'Red Hat', 'MongoDB')

    #PUNTO 4
    print('\nARBOL DE EXPANCION MINIMA')
    grafo.prim()
    
    #PUNTO 5
    print('\nQUITAR IMPRESORA')
    grafo.eliminar_vertice('Impresora')
    print('\nBARRIDO EN PROFUNDIDAD')
    grafo.barrido_profundidad(0)
    
ejercicio()