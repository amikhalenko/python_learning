#результат работы функций не выведется при включенной проверке условия if __name__ == '__main__': в файлах salary.py и people.py
from application.salary import calculate_salary as sal
from application.db.people import get_employees as emp

def main():
    print('С добрым утром!')

if __name__ == '__main__':
    sal()
if __name__ == '__main__':
    emp()
if __name__ == '__main__':
    main()


