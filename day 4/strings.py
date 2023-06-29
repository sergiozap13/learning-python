multiline_string = '''
    hello, this is a multilne string.
'''
# para concatenar string se usa el +
"""
Secuencias de espacio: 

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH # Para revertir un string
"""

# Exercises day 4

concatenated_string = 'Thirty ' + 'Days ' + 'Of ' + 'Python '
print(concatenated_string)
company = 'Coding For All'
print(len(company))
company = company.upper()
print(company)  
company = company.lower()
print(company)  
company = company.capitalize()
print(company)
first_word = company[0:6]
print(first_word)
print(company.index('a'))
company_python = company.replace('Coding', 'Python')
print(company_python)
splited_company = company.split(' ')
print(splited_company)
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[-1])
print(company[10])
python_everyone = 'Python For Everyone'
print(python_everyone[0] + '.' + python_everyone[7] + '.' + python_everyone[11])
print( 'You cannot end a sentence with because because because is a conjunction'.find('because'))
print( 'You cannot end a sentence with because because because is a conjunction'[31:54])
print('   Coding For All      '.strip(' '))
lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(lista))
radius = 10
area = 3.14 * radius ** 2
print('The area of circle with radius {} is {} meters square'.format(radius,int(area)))