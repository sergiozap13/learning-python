"""
En python tenemos el if / else 
    a = 3
    if a < 0:
        print('A is a negative number')
    else:
        print('A is a positive number')

Si necesitamos mas condiciones, en vez de encadenar else if como en java, se usa el elif:
    if condition:
        code
    elif condition:
        code
    else:
        code
    
Se puede hacer algo así parecido a un ternario: 
    a = 3
    print('A is positive') if a > 0 else print('A is negative')
    
Se usan los operadores logicos and y or
    if condition and condition:
        code
    if condition or condition:
        code
"""
#Ejercicios level 1 

# age = int(input('Enter your age: '))
# if age > 18:
#     print('You are old enough to learn to drive.')
# else:
#     print('You need {} more years to learn to drive.'.format(18 - age))
    
# Ejercicios level 2

"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
# alumn_score = int(input('enter your math score: '))
# grade = 'F'
# if(alumn_score >= 80):
#     grade = 'A'
# elif(alumn_score >= 70 and alumn_score < 90):
#     grade = 'B'
# elif(alumn_score >= 60 and alumn_score < 70):
#     grade = 'C'
# elif(alumn_score >= 50 and alumn_score < 60):
#     grade = 'D'

# print('your grade is {}'.format(grade))

# Ejercicios level 4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if(person.get('skills')):
    skills_list = person['skills']
    print(skills_list[int(len(skills_list)/2)])
    if('Python' in skills_list):
        print('This person has Python skills')
        
if person['is_marred']  and person['country'] == 'Finland':
    name = person['first_name']
    country = person['country']
    print('{} lives in {}. He is married.'.format(name, country))
    