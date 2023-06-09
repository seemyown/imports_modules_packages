import datetime as dt

from passlib.context import CryptContext

from application.salary import calculate_salary
from application.db.people import get_employees


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pass(passowrd):
    return pwd_context.hash(passowrd)

if __name__ == '__main__':
    print(f"Current date: {dt.datetime.now()}")
    pwd = input("Введите пароль: ")
    print(f"Ваш захэшированный пароль {hash_pass(pwd)}") 
    get_employees()
    calculate_salary()