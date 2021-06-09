import sqlite3
import inquirer
import os

class Nurse:
    def __init__(self, name, family, nurse_id):
        self.name = name
        self.family = family
        self.nurse_id = nurse_id
    
    def brief(self):
        os.system('cls')
        pass

    def add_workplace(self, workplace = True):
        os.system('cls')
        questions = insert_data(workplace = workplace)
        answers = inquirer.prompt(questions)
        city = answers['city']
        hospital = answers['hospital']
        ward = answers['ward']
        execute('INSERT INTO Workplaces VALUES ("%s", "%s", "%s")' % (city, hospital, ward))

    def del_workplace(self):
        os.system('cls')
        wp_list = execute('SELECT * FROM Workplaces')
        if wp_list:
            questions = [inquirer.List(
                'Workplaces',
                message= 'Select a Workplace',
                choices= wp_list
            )]
            answers = inquirer.prompt(questions)
            city = answers['Workplaces'][0]
            hospital = answers['Workplaces'][1]
            ward = answers['Workplaces'][2]
            execute("DELETE FROM Workplaces WHERE city = '%s' AND hospital = '%s' AND ward = '%s'" 
            % (city, hospital, ward))
        else:
            print('You don\'t define any workplace')

    def add_shift(self, workplace = True, date = True, shift = True):
        os.system('cls')
        select_wp = select_data(workplace)
        wp = inquirer.prompt(select_wp)
        if wp['workplace'] != '* New workplace':
            city = wp['workplace'][0]
            hospital = wp['workplace'][1]
            ward = wp['workplace'][2]
            workplace = False
        questions = insert_data(workplace, date, shift)
        answers = inquirer.prompt(questions)
        if workplace:
            city = answers['city']
            hospital = answers['hospital']
            ward = answers['ward']
            execute('INSERT INTO Workplaces VALUES ("%s", "%s", "%s")' % (city, hospital, ward))
        year = int(int(answers['year']))
        month = int(int(answers['month']))
        day = int(int(answers['day']))
        shift = answers['shift']
        holiday = answers['holiday']
        execute(f'INSERT INTO Shifts VALUES ("%s", "%s", "%s", %i, %i, %i, "%s", "%s")'
         % (city, hospital, ward, year, month, day, shift, holiday))

    def del_shift(self, date = True):
        os.system('cls')
        check_shifts = execute('SELECT * FROM Shifts')
        if check_shifts:
            questions = select_data(date = date)
            answers = inquirer.prompt(questions)
            city = answers['selected_shift'][0]
            hospital = answers['selected_shift'][1]
            ward = answers['selected_shift'][2]
            year = int(answers['selected_shift'][3])
            month = int(answers['selected_shift'][4])
            day = int(answers['selected_shift'][5])
            shift = answers['selected_shift'][6]
            holiday = answers['selected_shift'][7]
            execute(f'''DELETE FROM Shifts 
            WHERE city = "%s" AND hospital = "%s" AND ward = "%s" 
            AND year = %i AND month = %i AND day = %i
            And shift = "%s" AND holiday = "%s"''' 
            % (city, hospital, ward, year, month, day, shift, holiday))
        else:
            print('You don\'t save any shift yet.')

    def edit_shift(self):
        pass

    def workplaces_list(self):
        os.system('cls')
        workplaces = execute('SELECT * FROM Workplaces')
        if workplaces:
            for wp in workplaces:
                print(wp)
        else:
            print('You don\'t define any workplace yet.')

    def select_month(self, year, month):
        os.system('cls')
        shifts = execute(f'SELECT * FROM Shifts WHERE year = %i And month = %i' % (year, month))
        if shifts:
            for shift in shifts:
                city, hospital, ward, year, month, day, shift, holiday = shift
                print(f' - %i/%i/%i: %s holiday: %s (%s - %s: %s)' % (year, month, day, shift, holiday, city, hospital, ward))
        else:
            print('You don\'t save any shift in that month.')

def execute(text):
    cnx = sqlite3.connect('./data.db')
    cursor = cnx.cursor()
    cursor.execute(text)
    content = [x for x in cursor] or None
    cnx.commit()
    cnx.close()
    return content

def insert_data(workplace = False, date = False, shift = False, user = False):
    questions = []
    if workplace:
        questions.append(
            inquirer.Text("city", message="City")
        )
        questions.append(
            inquirer.Text("hospital", message="Hospital name")
        )
        questions.append(
            inquirer.Text("ward", message="Ward")
        )
    if date:
        questions.append(
            inquirer.Text("year", message="year")
        )
        questions.append(
            inquirer.Text("month", message="month")
        )
        questions.append(
            inquirer.Text("day", message="day"),
        )
    if shift:
        questions.append(
            inquirer.Checkbox(
                'shift',
                message= 'Check shift(s)',
                choices= ['M', 'E', 'N']
            )
        )
        questions.append(
            inquirer.List(
                "holiday",
                message="Is it a holiday?",
                choices= ['Yes', 'No']
            )
        )
    if user:
        questions.append(
            inquirer.Text("name", message="Mame")
        )
        questions.append(
            inquirer.Text("family", message="Family")
        )
        questions.append(
            inquirer.Text("nurse_id", message="Nursing id"),
        )
    return questions

def select_data(workplace = False, date = False):
    questions = []
    if workplace == True:
        workplaces = execute('SELECT * FROM Workplaces') or []
        workplaces.append('* New workplace')
        questions.append(
            inquirer.List(
                'workplace',
                message= "Select workplace",
                choices= workplaces
            )
        )
    if date:
        while True:
            query = [
                inquirer.Text("year", message="year"),
                inquirer.Text("month", message="month"),
                inquirer.Text("day", message="day"),
            ]
            answers = inquirer.prompt(query)
            year = int(answers['year'])
            month = int(answers['month'])
            day = int(answers['day'])
            all_shifts = execute(f'SELECT * FROM Shifts WHERE year = %i AND month = %i AND day = %i ' % (year, month, day))
            if all_shifts:
                questions.append(
                    inquirer.List(
                        'selected_shift',
                        message= "Select a shift",
                        choices= all_shifts
                    )
                )
                break
            else:
                print(' You don\'t save any shift in this date.')
    return questions

def help():
    print('''------------------------------------------------------
                         Help
------------------------------------------------------
- brief         See brief of your shift records
- add           Add new shift to database
- del           Del a shift from database
- edit          Edit a shift from database
- wp            See list og workplaces
- add-wp        Define new workplace
- del-wp        Delete defined workplace
- month         Select an show shifts of a month
------------------------------------------------------''')