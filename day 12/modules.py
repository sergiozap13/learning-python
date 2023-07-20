"""

Un módulo es un archivo que contiene código que puede ser incluido en una aplicación. 

Para crear un módulo, escribimos nuestro codigo y lo guardamos en un archivo. (mi_modulo.py)

Para importar un modulo, usamos la palabra reservada import

Podemos importar solo funciones o solo variables: 

from mymodule import generate_full_name, sum_two_nums, person, gravity

Podemos renombrar el nombre del modulo para que sea más facil trabajar con el: 

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

Vemos alguno de los modulos mas importantes:

- Os Module: Nos da funciones para crear, cambiar o borrar directorios...

- Sys Module: Nos da funciones para manipular diferentes partes del entorno de ejecución de python. Por ejemplo, la funcion sys.argv
devuelve una lista de argumentos que se le pasan a un script de python. 

- Statistics module: nos aporta funciones para estadisticas matematicas de datos numericos. Las más populares son: mean. median, mode...

- Math module: Contiene varias operaciones y constantes matematicas.
Si queremos importar todas las funciones del modulo, usamos: from math import *

- String module: Es un útil módulo que se usa para manejar strings.

- Random module: Tiene muchas funciones pero solo veremos random(entre 0 y 0.9999) y randomint (un entero aleatorio entre 2)

"""

import mi_modulo
import random
print(mi_modulo.generar_full_name('Sergio', 'Zapata'))

# Ejercicio 3
def shuffle_list(list):
    return random.shuffle(list)

lista1 = [1,2,3,4,5,6,7,8]
shuffle_list(lista1)
print(lista1)

def random_numbers_list():
    lista2 = []
    while(len(lista2) < 7): 
        numero = random.randint(0,9)
        if(numero not in lista2):
            lista2.append(numero) 
    return lista2

print(random_numbers_list())