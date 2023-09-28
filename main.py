from os import path
from Application.salary import calculate_salary
from Application.db.people import get_employees
from datetime import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dt = datetime.today().strftime("%d.%m.%Y")
    print(f"Сегодня {dt}")
    calculate_salary()
    get_employees()