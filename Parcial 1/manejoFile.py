from tdaLista import Lista

def cargarLLista(jedis):
    file = open('jedis.txt')

    lineas = file.readlines()
    lineas.pop(0)
    for linea in lineas:
        jedi = linea.split(';')
        # print(jedi)
        jedi_data = {}
        jedi_data['name'] = jedi[0].title()
        jedi_data['rank'] = jedi[1]
        jedi_data['species'] = jedi[2]
        jedi_data['master'] = jedi[3].split('/')
        jedi_data['lightsaber_color'] = jedi[4].split('/')
        jedi_data['homeworld'] = jedi[5]
        jedi_data['birth_year'] = jedi[6]
        jedi_data['height'] = float(jedi[7].split('\n')[0])
        if(len(jedi) > 8):
            jedi_data['to_darkside'] = jedi[8]
            jedi_data['come_lightside'] = jedi[9]
        jedis.insertar(jedi_data, 'name')


    file.close()