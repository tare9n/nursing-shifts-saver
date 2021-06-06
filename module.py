import sqlite3

class Nurse:
    def __init__(self, name, family, nurse_id):
        self.name = name
        self.family = family
        self.nurse_id = nurse_id

    def add_workplace(self, city, hospital, ward):
        execute('INSERT INTO Workplaces VALUES (%s, %s, %s)' % (city, hospital, ward))

    def make_shift_id(self):
        pass

    def add_shift(self, id, city, hospital, ward, year, month, day, shift, holiday = 'No'):
        execute(f'INSERT INTO Shifts VALUES (%s, %s, %s, %i, %i, %i, %s, %s)'
         %(id, city, hospital, ward, year, month, day, shift, holiday))

    def del_shift(self):
        pass

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