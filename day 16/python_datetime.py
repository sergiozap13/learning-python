"""

Python tiene un modulo para las fechas.
    import datetime

Con dir, podemos ver las funciones que existen en un modulo.
    print(dir(datetime)) -> nos daría una lista con todas las funciones

Para obtener información sobre la fecha de hoy:

    from datetime import datetime
    now = datetime.now
    day = now.day
    timestamp = datetime.timestamp() -> Devuelve el numero de segundos pasados desde el 1 de enero de 1970

Para formatear las fechas:
    from datetime import datetime
    new_year = datetime(2022, 1,1)
    print(new_year)      # 2022-01-01 00:00:00
    day = new_year.day

Se puede usar el metodo strftime para formatear fechas: 
    from datetime import datetime
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    print("time:", t)
    
Pasar un string a fecha con strptime: 
    from datetime import datetime
    date_string = "5 December, 2019"
    print("date_string =", date_string)
    date_object = datetime.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)

Si usamos date de datetime: 
    from datetime import date
    d = date(2020, 1, 1)
    print(d)
    print('Current date:', d.today())    # 2019-12-05
    # date object of today's date
    today = date.today()
    print("Current year:", today.year)   # 2019
    print("Current month:", today.month) # 12
    print("Current day:", today.day)     # 5
    
Con Time podemos representar el tiempo

Con date, podemos hacer restas entre 2 tiempos:
    today = date(year=2019, month=12, day=5)
    new_year = date(year=2020, month=1, day=1)
    time_left_for_newyear = new_year - today
    # Time left for new year:  27 days, 0:00:00
"""

# Ejercicios
from datetime import datetime

now = datetime.now()
print("Ahora:", now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

format = now.strftime("%m/%d/%Y, %H:%M:%S")

print("Fecha formateada", format)

# today = "5 December 2019"

# date_object_today = datetime.strptime(today,  "%d %m %y")
# print("Date object", date_object_today)

new_year = datetime(2023,1,1)
difference = now - new_year
print(difference)