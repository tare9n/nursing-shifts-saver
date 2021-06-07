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

    def add_shift(self, workplase = False, date = True, shift = True):
        select_wp = select_data()
        workplase = inquirer.prompt(select_wp)
        if workplase != '* New workplase':
            city = workplase['workplase'][0]
            hospital = workplase['workplase'][1]
            ward = workplase['workplase'][2]
            workplase = False
        else:
            workplase = True
        questions = insert_data(workplase, date, shift)
        answers = inquirer.prompt(questions)
        if city in answers.keys():
            city = answers['city']
            hospital = answers['hospital']
            ward = answers['ward']
        year = answers['year']
        month = answers['month']
        day = answers['day']
        shift = answers['shift']
        holiday = answers['holiday']
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

def execute(text):
    cnx = sqlite3.connect('./data.db')
    cursor = cnx.cursor()
    cursor.execute(text)
    content = [x for x in cursor] or None
    cnx.commit()
    cnx.close()
    return content

def insert_data(workplase = False, date = False, shift = False):
    questions = []
    if workplase:
        questions.append(
            inquirer.Text("city", message="City: "),
            inquirer.Text("hospital", message="Hospital name: "),
            inquirer.Text("ward", message="Ward: "),
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
            ),
            inquirer.List(
                "holiday",
                message="Is it a holiday?",
                choices= ['Yes', 'No']
            )
        )
    return questions

def select_data():
    questions = []
    workplases = execute('SELECT * FROM Workplaces')
    workplases.append('* New workplase')
    questions.append(
        inquirer.List(
            'workplase',
            message= "Select workplase: ",
            choices= workplases
        )
    )
    return questions

def help():
    print('''------------------------------------------------------
                         Help
------------------------------------------------------
- brief         See brief of your shift records
- add           Add new shift to database
- del           Del a shift from database
- edit          Edit a shift from database
- wp            See list og workplases
- add wp        define new workplase
- month         Select an show shifts of a month
------------------------------------------------------''')