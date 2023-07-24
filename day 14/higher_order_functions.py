"""

Higher order functions: funciones de orden superior. Las funciones pueden tener funciones como parámetro. Puede serr devuelta
como el resultado de otra función. Puede ser modificada y puede ser asignada a una variable.

Funciones como parametro: 

    def sum_numbers(nums):  # normal function
        return sum(nums)    # a sad function abusing the built-in sum function :<

    def higher_order_function(f, lst):  # function as a parameter
        summation = f(lst)
        return summation
    result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
    
Los cierres en python, permiten que una función anidada acceda al ámbito de la función envolvente:
    def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

    closure_result = add_ten()

Los decoradores en python son patrones de diseño que permiten al usuario aádir una nueva funcionabilidad a un objeto,
sin modificar su estructura. 

Para crear un decorador tenemos que crear una función externa que tenga una función contenedora interna: 
    def uppercase_decorator(function):
        def wrapper():
            func = function()
            make_uppercase = func.upper()
            return make_uppercase
        return wrapper

Una vez tenemos el decorador hecho, se usa utilizando el @ con el nombre del decorador.
En este caso:
    @uppercase_decorator
    def greeting():
        return 'Texto'

"""
