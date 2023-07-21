"""

La comprensión de listas es una forma compacta de crear lista a partir de una secuencia. Es más rápido que procesar
una lista con un for. 
La sintaxis es: 
    [i for i in iterable if expression]

Por ejemplo si queremos cambiar un string a una lista de caracteres: 

    language = 'Python'
    lst = list(language) -> sería una forma
    lst = [i for i in language] -> segunda forma, más rápido. 

Se pueden combinar con expresiones: 
    even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
    print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


Una función lambda es una función anónima sin nombre. Sirve para escribir una función dentro de otra y estas pueden recibir
tantos parametros como se quiera, pero solo una expresión.

Se usa la palabra reservada lambda. 

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

Es como usar una variable como si fuera una función y le podemos pasar tantos params como queramos. 

"""

#Ejercicios 

# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [i for i in numbers if i <= 0]

print(numbers)