"""

SyntaxError -> Suele ocurrir si tenemos un fallo en la sintaxis. Por ejemplo si no usamos parentesis para un print

    print 'hello world'

NameError -> Ocurre cuando intentamos ver el contenido de una variable que no está definida. 

    print(age)
    

IndexError -> Pasa si intentamos acceder a una posición de un array que está fuera de los limites de este.
    numbers = [1, 2, 3, 4, 5]
    numbers[5]
    
ModuleNotFoundError -> Ocurre si intentamos importar un modulo que no existe. 
    import math
    
AttributeError -> Cuando una función no existe. 
    math.PI
Lo correcto seria:
    math.pi

KeyError -> Si intentamos acceder a una clave de un diccionario y no existe. 
    user = {'name':'Asab', 'age':250, 'country':'Finland'}
    user['county']
    
TypeError -> Cuando intentamos usar una función sobre un tipo de dato no compatible para esta. Por ejemplo, si intentamos
sumar un entero con un string. 
    4 + '3'

ImportError -> Si intentamos importar una funcion que no existe en el modulo especificado
    from math import power
    
ValueError -> Por ejemplo, si intentamos transformar a entero un string: 
    int('12a')

ZeroDivisionError -> Si se intenta dividir entre 0. En python no se puede dividir por 0. 
    1/0
"""