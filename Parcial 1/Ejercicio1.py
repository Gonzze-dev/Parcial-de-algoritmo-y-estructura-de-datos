def recorrerVector(vector):
    if len(vector) == 0:
        return None
    else:
        if (vector[-1] == 'Yoda'):
            return len(vector)

        return recorrerVector(vector[:-1])

def ejercicio1():
    jedis = ['Yoda','','','','']
    pos = recorrerVector(jedis)

    if pos is not None:
        pos = pos - 1
        print('Yoda esta en la posicion: ', pos)
    else:
        print('Yoda no se encuentra en el vector')


ejercicio1()