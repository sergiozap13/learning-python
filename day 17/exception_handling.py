"""

Al igual que en Java, en python podemos manejar las excepciones con el siguiente bloque de codigo:
    try:
        code in this block if things go well
    except:
        code in this block run if things go wrong
Por ejemplo: 
    try:
        print(10 + '5')
    except:
        print('Something went wrong')
    
Podemos especificar la excepción para poder cubrir varias de estas en un mismo try: 
    try:
        name = input('Enter your name:')
        year_born = input('Year you were born:')
        age = 2019 - year_born
        print(f'You are {name}. And your age is {age}.')
    except TypeError:
        print('Type error occured')
    except ValueError:
        print('Value error occured')
    except ZeroDivisionError:
        print('zero division error occured')
    
Se pueden añadir los bloques else y finally para realizar distintas ejecuciones segun nos convenga: 
    except ZeroDivisionError:
        print('zero division error occur')
    else:
        print('I usually run with the try block')
    finally:
        print('I alway run.')

En ptyhon podemos empaquetar y desempaquetar argumentos: 
Se usan dos operadores:
    * Para tuplas
    ** Para diccionarios
    
Desempaquetando listas: 
    def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

    lst = [1, 2, 3, 4, 5]
    print(sum_of_five_nums(*lst)) -> para poder pasarle 5 parametros y no tener que escribir cada uno de ellos.

Con los diccionarios:
    def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
    dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
    print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
    
Empaquetando listas: A veces no sabemos cuantos argumentos va necesitar la función que estamos creando:
   def sum_all(*args):
        s = 0
        for i in args:
            s += i
        return s 

El spreading en Python funciona de la siguiente forma:
    country_lst_one = ['Finland', 'Sweden', 'Norway']
    country_lst_two = ['Denmark', 'Iceland']
    nordic_countries = [*country_lst_one, *country_lst_two]

Se puede usar el metodo enumerate para obtener el indice de cada item de la lista:
    for index, i in enumerate(countries):
        print('hi')
        if i == 'Finland':
            print('The country {i} has been found at index {index}')

Podemos combinar listas con el zip. Por ejemplo, podemos combinar listas para recorrerlas juntas:

    fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
    vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
    fruits_and_veges = []
    for f, v in zip(fruits, vegetables):
        fruits_and_veges.append({'fruit':f, 'veg':v})

    print(fruits_and_veges) 
    [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
"""

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries, es, ru = names

print(nordic_countries, es, ru)