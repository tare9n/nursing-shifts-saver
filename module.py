import sqlite3
import inquirer
from inquirer import questions

class Nurse:
    def __init__(self, name, family, nurse_id):
        self.name = name
        self.family = family
        self.nurse_id = nurse_id

    def add_workplace(self, city, hospital, ward):
        execute('INSERT INTO Workplaces VALUES (%s, %s, %s)' % (city, hospital, ward))

    def add_shift(self, city, hospital, ward, year, month, day, shift, holiday = 'No'):
        execute(f'INSERT INTO Shifts VALUES (%s, %s, %s, %i, %i, %i, %s, %s)'
         %(city, hospital, ward, year, month, day, shift, holiday))

    def del_shift(self, year, month, day):
        execute(f'SELECT * FROM Shifts WHERE year = %i AND month = %i AND day = %i' % (year, month, day))

    def edit_shift(self):
        pass

    def workplaces_list(self):
        workplaces = execute('SELECT * FROM Workplace')
        return workplaces

    def select_month(self):
        pass

    def help(self):
        print('''------------------------------------------------------
                            Help
    ------------------------------------------------------
    - brief         See brief of your shift records
    - add           add
    - del           del
    - edit          edit
    - wards         wards
    - month         select
    ------------------------------------------------------''')


def execute(text):
    cnx = sqlite3.connect('./data.db')
    cursor = cnx.cursor()
    cursor.execute(text)
    content = [x for x in cursor] or None
    cnx.commit()
    cnx.close()
    return content

def input_data(workplase = False, date = False, shift = False):
    questions = []
    if workplase:
        workplases = execute('SELECT * FROM Workplaces')
        workplases.append('* New workplase')
        questions.append(
            inquirer.List(
                'workplase',
                message= "Select workplase: ",
                choices= workplases
            )
        )
    if date:
        questions.append(
            inquirer.Text("year", message="year: "),
            inquirer.Text("month", message="month: "),
            inquirer.Text("day", message="day: "),
            )
    if shift:
        questions.append(
            inquirer.Checkbox(
                'shift',
                message= 'Check shift(s): ',
                choices= ['M', 'E', 'N']
            )
        )
    return questions