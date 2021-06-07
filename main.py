from module import *

execute('''CREATE TABLE IF NOT EXISTS Shifts 
        (hospital TEXT, unit TEXT, year NUMBER, month NUMBER, day NUMBER, shift TEXT, holiday TEXT)''')

execute('''CREATE TABLE IF NOT EXISTS Workplaces 
        (city TEXT, hospital TEXT, unit TEXT)''')