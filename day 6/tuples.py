"""
Las tuplas son inmutables y ordenadas. 
Los metodos de las tuplas son: 
- tuple() -> para crear ua tupla vacia
- count() -> para contar el numero de un item en la tupla
- index() -> para buscar el indice de un item de la tupla
"""

tupla_vacia = ()
# or
tupla_vacia_2 = tuple()

# Se puede acceder a los elementos por indexacion
# Se hace slice de la misma forma que en las listas [initial, final]
# Podemos cambiar de una tupla a una lista:

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print('orange' in fruits) # True. Para ver si el elemento está en la tupla

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)