"""
Los sets son conjuntos de elementos únicos desordenados y sin indice. 
Para crear un set:
- st = set()
- st = {1,2,3}

Para ver si un elemento está en el set, se usa el operador 'in'
Para añadir un elemento se usa el add(item), o si queremos añadir varios: st.update(['item5','item6','item7'])

borrar: st.remove('item2')
para quedarnos con el elemento borrado: removed_item = fruits.pop() 

Para borrar el set completo:
    fruits = {'banana', 'orange', 'mango', 'lemon'}
    del fruits
Podemos convertir una lista en un set y los elementos repetidos se eliminarán
    lst = ['item1', 'item2', 'item3', 'item4', 'item1']
    st = set(lst)
Para juntar sets se usa el metodo union(). Se puede hacer también la operación intersección
    st3 = st1.union(st2)
Se usa el metodo isdisjoint y es true si los sets son totalmente distintos. 
"""

# EJERCICIOS    
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# level 1
print(len(it_companies))
it_companies.add('Threads')
it_companies.update('Twitter' , 'Logitech')
it_companies.remove('IBM')
# level 2 
A.union(B)
print(A.intersection(B))
print(A.isdisjoint(B))

del A, B    

# level 3
age_list = set(age)
print(len(age_list),' ',len(age))
phrase = 'I am a teacher and I love to inspire and teach people'
# obtener un set con las palabras unicas de la frase:
phrase_set = set(phrase.split(' '))
print(phrase_set)