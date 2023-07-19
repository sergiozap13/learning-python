"""

Las funciones se declaran con la palabra reservada def. 

    def add_two_numbers ():
        num_one = 2
        num_two = 3
        total = num_one + num_two
        print(total)
    add_two_numbers()

Se pueden devolver variables con el return
    def add_two_numbers ():
        num_one = 2
        num_two = 3
        total = num_one + num_two
        return total
    add_two_numbers()

Podemos pasarle parametros a las funciones:
    # Declaring a function
    def function_name(parameter):
        codes
        codes
    # Calling function
    print(function_name(argument))
  
Se pueden pasar los argumentos asi, y no importa el orden en el que los pases: 
    def add_two_numbers (num1, num2):
        total = num1 + num2
        print(total)
    print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
    
Podemos tener funciones con un numero indefinido de argumentos: CON *
    def sum_all_nums(*nums):
        total = 0
        for num in nums:
            total += num     # same as total = total + num 
        return total
    print(sum_all_nums(2, 3, 5)) # 10
"""

# Ejercicios level 1:
def capitalize_list_items(list):
    capitalize_list_items = []
    for item in list:
        capitalize_list_items.append(item.capitalize())
    return capitalize_list_items

lista1 = ['hola', 'soy', 'sergio']
print(capitalize_list_items(lista1))

def sum_of_even(last):
    counter = 0
    for i in range(last):
        if i % 2 == 0:
            counter += i
    return counter
print(sum_of_even(50))

# Ejercicios level 2:

def evens_and_odds(num):
    evens_counter = 0
    odds_counter = 0
    for i in range(0,num + 1):
        if i % 2 == 0:
            evens_counter += 1
        else:
            odds_counter += 1
    print('Even numbers: {}'.format(evens_counter))
    print('Odds numbers: {}'.format(odds_counter))
evens_and_odds(100)

# Ejercicios level 3

def same_data(list):
    same = True
    for i in range(0, len(list) - 1):
        if(type(list[i]) != type(list[i+1])):
            same = False
    return same

lista2 = [1,2,3,34,4,6]
print( same_data(lista2))
      
