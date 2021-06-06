from module import *

execute('''CREATE TABLE IF NOT EXISTS Shifts 
        (id TEXT NOT NULL PRIMARY KEY, hospital TEXT, unit TEXT, year NUMBER, month NUMBER, day NUMBER, shift TEXT, holiday TEXT)''')

execute('''CREATE TABLE IF NOT EXISTS Workplaces 
        (city TEXT, hospital TEXT, unit TEXT)''')



# while True:
#     while True:
#         request = input('> ')
#         if request in ('add', 'del', 'brief', )