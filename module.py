import sqlite3

class nursingShifts:
    def __init__(self):
        pass

    def add_hospital(self):
        pass

    def add_unit(self):
        pass

    def make_shift_id(self):
        pass

    def add_shift(self, id, hospital, unit, year, month, day, shift, holiday = 'No'):
        execute(f'INSERT INTO Shifts VALUES (%s, %s, %i, %i, %i, %s, %s)' %(id, hospital, unit, year, month, day, shift, holiday))

    def del_shift(self):
        pass

    def edit_shift(self):
        pass

    def hospitals_and_units_list(self):
        pass

    def select_month(self):
        pass

    def help(self):
        print('''------------------------------------------------------
                            Help
    ------------------------------------------------------
    - brief         See brief of your shift records
    - add
    - del
    - edit
    - units
    - month
    ------------------------------------------------------''')


def execute(text):
    cnx = sqlite3.connect('./data.db')
    cursor = cnx.cursor()
    cursor.execute(text)
    cnx.commit()
    cnx.close()

def select(text):
    cnx = sqlite3.connect('./data.db')
    cursor = cnx.cursor()
    cursor.execute(text)
    content = [x for x in cursor]
    cnx.close()
    return content