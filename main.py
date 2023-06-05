import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

import pyjokes


def start_program(user, password):
    print(f'Hi, {user}!')
    print(datetime.datetime.now().strftime("%d.%m.%Y"))
    return


def get_pyjoke():
    print(pyjokes.get_joke())
    return


if __name__ == '__main__':
    start_program('user', 'qwerty')
    calculate_salary(45, 54)
    get_employees()

    get_pyjoke()
