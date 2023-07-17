"""
Un diccionario es una coleccion de elementos desordenados, modificables y pareables. Se corresponde con el map de otros lenguajes

Usa clave/valor

Para crear un diccionario: 
    empty_dict = {}
    dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
    
Para acceder a los valores:
print(dct['key1']) # value1

Es mejor usar el metodo get, por si la clave no existe: 
print(person.get('first_name')) # Asabeneh
print(person.get('city'))   # None -> si no existe, devuelve NONE

Para añadir un par: 
    dct['key5'] = 'value5'
Para comprobar que existe un elemento en el diccionario
    print('key2' in dct) # True
    
Se puede cambiar un diccionario a una lista de tuplas con el metodo items()
    dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
    # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
    
Para obtener una lista de las claves de nuestro diccionario: 
    keys_list = dct.keys()
Lo mismo para los valores: 
    values_list = dct.values()
"""

dic = {'Sergio':'Zapata', 'Amaia':2}
print(dic['Amaia']) # se accede al valor de la clave
dic_keylist = dic.keys()
dic_veluelist = dic.values()

dic_tuple = dic.items()
print('Sergio' in dic_tuple)

del dic
